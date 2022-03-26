import os
import pymongo
import unittest
from modules.background_tasks.translate_file_created_by_public_request.translate_content.docx.main import *

async def test_read_task_result():
    test1 = read_task_result(tasks_result = [], tasks = [], translations_history = [])
    print(test1)

    test2 = read_task_result(tasks_result = ['sample1.docx'], tasks = ['sample1.docx'], translations_history = ['sample1.docx'])
    print(test2)

    test3 = read_task_result(tasks_result = ['sample2.docx'], tasks = ['sample2.docx'], translations_history = ['sample2.docx'])
    print(test3)

    test4 = read_task_result(tasks_result = ['sample3.docx'], tasks = ['sample3.docx'], translations_history = ['sample3.docx'])
    print(test4)

    test5 = read_task_result(tasks_result = ['sample4.docx'], tasks = ['sample4.docx'], translations_history = ['sample4.docx'])
    print(test5)

async def test_execute_in_batch():
    test1 =  execute_in_batch(valid_tasks_mapper = [], tasks_id = [], allowed_concurrent_request = [])
    print(test1)

    test2 =  execute_in_batch(valid_tasks_mapper = ['sample1.docx'], tasks_id = ['sample1.docx'], allowed_concurrent_request = ['sample1.docx'])
    print(test2)

    test3 =  execute_in_batch(valid_tasks_mapper = ['sample2.docx'], tasks_id = ['sample2.docx'], allowed_concurrent_request = ['sample2.docx'])
    print(test3)

    test4 =  execute_in_batch(valid_tasks_mapper = ['sample3.docx'], tasks_id = ['sample3.docx'], allowed_concurrent_request = ['sample3.docx'])
    print(test4)

    test5=  execute_in_batch(valid_tasks_mapper = ['sample4.docx'], tasks_id = ['sample4.docx'], allowed_concurrent_request = ['sample4.docx'])
    print(test5)

async def test_mark_invalid_tasks():
    test1 = mark_invalid_tasks(invalid_tasks_mapper = [])
    print(test1)

    test2 = mark_invalid_tasks(invalid_tasks_mapper = ['sample1.docx'])
    print(test2)

    test3 = mark_invalid_tasks(invalid_tasks_mapper = ['sample2.docx'])
    print(test3)

    test4 = mark_invalid_tasks(invalid_tasks_mapper = ['sample3.docx'])
    print(test4)

    test5 = mark_invalid_tasks(invalid_tasks_mapper = ['sample4.docx'])
    print(test5)

async def test_main(self):
    test = os.system('main.py')
    self.assertEqual(test, 0)
