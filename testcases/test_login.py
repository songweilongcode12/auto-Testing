#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : Lenovo
# date: 2021/7/5 14:29
# version: 0.1
from tools.logger import Loggings
logger = Loggings()
import unittest
from tools.excel_util import excel_util
from Module.login import login
import json
class test_login(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_login(self):
        file = './../data/logindata.xlsx'
        excel = excel_util(file, 'Sheet1')
        testData = excel.next()
        logger.info(testData)
        run = login()
        result = run.login_success(url=testData[0]['url'],
                            data=json.loads(testData[0]['data']),
                            headers=json.loads(testData[0]['headers'])
                            )
        self.assertEqual('success',result['state'])