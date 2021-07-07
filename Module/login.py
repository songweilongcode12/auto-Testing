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
        logger.info(reponce)




if __name__=='__main__':
    file = './../data/logindata.xlsx'
    excel = excel_util(file, 'Sheet1')
    testData = excel.next()
    logger.info(testData)
    for i in range(len(testData)):
        url = testData[i]['url']
        data = testData[i]['data']
        headers = testData[i]['headers']
        id = testData[i]['ID']
        # logger.info(url)
        # logger.info(headers)
        # logger.info(data)
        # logger.info(id)
    # data = {
    #     "username": "admin",
    #     "password": "Abc@123789",
    #     "redirect": "http://192.168.3.151:8774/index.htm"
    # }
    # url = 'http://192.168.2.239:8770/login.json'
    # headers =  {
    #         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #         "User-Agent": "Mozilla/5.0 Chrome/52.0.2743.82 Safari/537.36"
    #     }
        runner = login()
        runner.login_success(url=url,
                             data=json.loads(data),
                             headers=json.loads(headers))