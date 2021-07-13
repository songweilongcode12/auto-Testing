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
from ddt import ddt,data
import json
@ddt
class test_login(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    filepath = r'D:\TestFiles\project\auto-Testing\data\logindata.xlsx'
    excel = excel_util(filepath, sheetName='Sheet1')
    testdata = excel.next()

    @data(*testdata)
    def test_01(self, iterm):
        data = json.loads(iterm['data'])
        headers = json.loads(iterm['headers'])
        url = iterm['url']
        runner = login()
        result = runner.login_success(
            url=url,
            data=data,
            headers=headers
        )
        setattr(runner,'token',result['token'])
        logger.info(hasattr(runner,'token'))
        logger.info(result)
        self.assertEqual('success',result['state'])
    # def test_02(self):
    #     a = login()
    #     # token = getattr(a,'token')
    #     logger.info(getattr(a,'token'))



if __name__=='__main__':
    unittest.main()



