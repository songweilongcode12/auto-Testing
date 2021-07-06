#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : Lenovo
# date: 2021/7/5 14:33
# version: 0.1
from tools.logger import Loggings
logger = Loggings()
from tools.Httprequest import httprequest
import json
import requests
from urllib import parse
# class login(httprequest):
#     def __init__(self):
#         self.token = None
#     def login_success(self):
#         data = {
#             "username": "admin",
#             "password": "Abc@123789",
#             "redirect": "http://192.168.3.151:8774/index.htm"
#         }
#         url = 'http://192.168.2.239:8770/login.json'
#         reponce = self.post(
#             url=url,
#             data=data,
#             dataform='form'
#         )
#         logger.info(reponce)

def login_success():
    data = {
        "username": "admin",
        "password": "Abc@123789",
        "redirect": "http://192.168.3.151:8774/index.htm"
    }
    url = 'http://192.168.2.239:8770/login.json'
    requestdata = parse(data)
    logger.info(requestdata)
    reponce = requests.post(
        url=url,
        data=requestdata,
        headers={
                            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"
        }
    )
    logger.info(reponce.text)


#
# if __name__=='__miin__':
# runner = login()
login_success()