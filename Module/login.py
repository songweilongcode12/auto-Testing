#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : Lenovo
# date: 2021/7/5 14:33
# version: 0.1
from tools.logger import Loggings
logger = Loggings()
from tools.Httprequest import httprequest
from tools.excel_util import excel_util

import json
class login(httprequest):
    def __init__(self):
        self.token = None
    def login_success(self,url,data,headers):
        reponce = self.postform(
            url=url,
            data=data,
            headers=headers
        )
        return reponce





if __name__=='__main__':
    file = './../data/logindata.xlsx'
    excel = excel_util(file, 'Sheet1')
    testData = excel.next()
    logger.info(testData)
    for i in range(len(testData)):
        url = testData[i]['url']
        data = testData[i]['data']
        headers = testData[i]['headers']
        runner = login()
        runner.login_success(url=url,
                             data=json.loads(data),
                             headers=json.loads(headers))
