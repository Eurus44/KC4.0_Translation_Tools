from modules.background_tasks.detect_plain_text_language_created_by_private_request.main import read_task_result, execute_in_batch, mark_invalid_tasks, main
from uuid import UUID
import pymongo
import asyncio
from core.utils.common import chunk_arr
from infrastructure.configs.task import (
    LanguageDetectionTaskNameEnum, 
    LanguageDetectionTaskStepEnum, 
    StepStatusEnum
)

from modules.language_detection_request.database.language_detection_request.repository import LanguageDetectionRequestRepository
from modules.language_detection_request.database.language_detection_request_result.repository import LanguageDetectionRequestResultRepository
from modules.language_detection_request.database.language_detection_history.repository import LanguageDetectionHistoryRepository

from modules.system_setting.database.repository import SystemSettingRepository

language_detection_request_repository = LanguageDetectionRequestRepository()
language_detection_request_result_repository = LanguageDetectionRequestResultRepository()
language_detection_history = LanguageDetectionHistoryRepository()
system_setting_repository = SystemSettingRepository()

async def test_read_task_result(ALLOWED_CONCURRENT_REQUEST):
    print('====TEST READ_TASK_RESULT FUNTION====')
    tasks = await language_detection_request_repository.find_many(
            params=dict(
                task_name=LanguageDetectionTaskNameEnum.private_plain_text_language_detection.value,
                current_step=LanguageDetectionTaskStepEnum.detecting_language.value,
                step_status=StepStatusEnum.not_yet_processed.value,
                # expired_date={
                #     "$gt": datetime.now()
                # }
            ),
            limit=ALLOWED_CONCURRENT_REQUEST
        )

    tasks_id = list(map(lambda task: task.id.value, tasks))

    tasks_result_and_trans_history_req = [
            language_detection_request_result_repository.find_many(
                params=dict(
                    task_id={
                        '$in': list(map(lambda t: UUID(t), tasks_id))
                    },
                    step=LanguageDetectionTaskStepEnum.detecting_language.value
                )
            ),
            language_detection_history.find_many(
                params=dict(
                    task_id={
                        '$in': list(map(lambda t: UUID(t), tasks_id))
                    }
                )
            )
        ]

    tasks_result, language_detections_history = await asyncio.gather(*tasks_result_and_trans_history_req)
    
    valid_tasks_mapper, invalid_tasks_mapper = await read_task_result(
            tasks=tasks, 
            tasks_result=tasks_result,
            language_detections_history=language_detections_history
        )
    print(f"result of valid_tasks_mapper: ", valid_tasks_mapper)
    print(f"result of invalid_tasks_mapper: ", invalid_tasks_mapper)
    return valid_tasks_mapper, invalid_tasks_mapper, tasks, ALLOWED_CONCURRENT_REQUEST


def test_mark_invalid_tasks(invalid_tasks_mapper):
    print('====TEST MARK_INVALID_TASKS FUNTION====')
    print("refult of test_mark_invalid_tasks: ", mark_invalid_tasks(invalid_tasks_mapper))

def test_execute_in_batch(valid_tasks_mapper, chucked_tasks_id, ALLOWED_CONCURRENT_REQUEST):
    print('====TEST EXECUTE_IN_BATCH FUNTION====')
    for chuck in chucked_tasks_id:
        execute_in_batch(valid_tasks_mapper, chuck, ALLOWED_CONCURRENT_REQUEST)

async def test_main():
    print('===TEST DETECT PLAIN TEXT LANGUAGE BY PUBLIC REQUEST===')
    system_setting = await system_setting_repository.find_one({})
    
    ALLOWED_CONCURRENT_REQUEST = system_setting.props.language_detection_api_allowed_concurrent_req
    
    if ALLOWED_CONCURRENT_REQUEST <= 0: return 
    valid_tasks_mapper, invalid_task_mapper, tasks = test_read_task_result(ALLOWED_CONCURRENT_REQUEST)
    test_mark_invalid_tasks(invalid_task_mapper)
    valid_tasks_id = list(map(lambda t: t.id.value, tasks))
    chunked_tasks_id = list(chunk_arr(valid_tasks_id, ALLOWED_CONCURRENT_REQUEST))
    test_execute_in_batch(valid_tasks_mapper, chunked_tasks_id, ALLOWED_CONCURRENT_REQUEST)

    print('====TEST MAIN FUNTION====')
    main()
    
