1.Trong file 'backend/src/tests/background_tasks/main.py' add:

    from tests.background_tasks.delete_invalid_file import add_fresh_jobs as add_fresh_jobs_01
    from tests.background_tasks.delete_invalid_file import add_fresh_jobs_2 as add_fresh_jobs_02 
    from tests.background_tasks.delete_invalid_file import add_fresh_jobs_3 as add_fresh_jobs_03
    from tests.background_tasks.delete_invalid_file import add_fresh_jobs_4 as add_fresh_jobs_04

    from tests.background_tasks.delete_invalid_task import add_fresh_jobs_1 as add_fresh_jobs_001
    from tests.background_tasks.delete_invalid_task import add_fresh_jobs_2 as add_fresh_jobs_002
    from tests.background_tasks.delete_invalid_task import add_fresh_jobs_3 as add_fresh_jobs_003

    BACKGROUND_TASKS = config.APP_CONFIG.TEST_BACKGROUND_TASKS

    new_background_task_scheduler = BackgroundTaskManager(AsyncIOScheduler())

    new_background_task_scheduler.remove_all_jobs()
    
    new_background_task_scheduler = add_fresh_jobs_01(new_background_task_scheduler, BACKGROUND_TASKS)

    new_background_task_scheduler = add_fresh_jobs_02(new_background_task_scheduler, BACKGROUND_TASKS)

    new_background_task_scheduler = add_fresh_jobs_03(new_background_task_scheduler, BACKGROUND_TASKS)

    new_background_task_scheduler = add_fresh_jobs_04(new_background_task_scheduler, BACKGROUND_TASKS)

    new_background_task_scheduler = add_fresh_jobs_001(new_background_task_scheduler, BACKGROUND_TASKS)

    new_background_task_scheduler = add_fresh_jobs_002(new_background_task_scheduler, BACKGROUND_TASKS)

    new_background_task_scheduler = add_fresh_jobs_003(new_background_task_scheduler, BACKGROUND_TASKS)
2.Trong file 'backend/src/infrastructure/configs/main.py' add:

        "test_get_file_created_time": BackgroundTask(
            ID="test_get_file_created_time",
            TRIGGER=BackgroundTaskTriggerEnum.interval.value,
            CONFIG=dict(seconds=0, max_instances=1),
        ),
        "test_main": BackgroundTask(
            ID="test_main",
            TRIGGER=BackgroundTaskTriggerEnum.interval.value,
            CONFIG=dict(seconds=0, max_instances=1),
        ),
        "test_get_to_be_deleted_file_path": BackgroundTask(
            ID="test_get_to_be_deleted_file_path",
            TRIGGER=BackgroundTaskTriggerEnum.interval.value,
            CONFIG=dict(seconds=0, max_instances=1),
        ),
        "test_get_task_id_from_task_result_file_path_delete_invalid_task": BackgroundTask(
            ID="test_get_task_id_from_task_result_file_path_delete_invalid_task",
            TRIGGER=BackgroundTaskTriggerEnum.interval.value,
            CONFIG=dict(seconds=0, max_instances=1),
        ),
        "test_main_delete_invalid_task": BackgroundTask(
            ID="test_main_delete_invalid_task",
            TRIGGER=BackgroundTaskTriggerEnum.interval.value,
            CONFIG=dict(seconds=0, max_instances=1),
        ),
        "test_get_to_be_deleted_file_path_delete_invalid_task": BackgroundTask(
            ID="test_get_to_be_deleted_file_path_delete_invalid_task",
            TRIGGER=BackgroundTaskTriggerEnum.interval.value,
            CONFIG=dict(seconds=0, max_instances=1),
        )