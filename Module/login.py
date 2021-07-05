#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : Lenovo
# date: 2021/7/5 14:33
# version: 0.1
from tools.logger import Loggings
logger = Loggings()
from tools.Httprequest import httprequest

class login(httprequest):
    def __init__(self):
        self.token = None
    def login_success(self):
        data = {
            "username": "admin",
            "password": "Abc@123789",
            "redirect": "http://192.168.3.151:8774/index.htm"
        }
        url = 'http://192.168.2.239:8770/login.json'
        reponce = self.post(
            url=url,
            data=data,
            dataform='form'
        )
        logger.info(reponce.text)

if __name__=='__miin__':
    runn = login()
    runn.login_success()