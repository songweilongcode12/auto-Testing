#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : Lenovo
# date: 2021/6/17 9:31
# version: 0.1

from tools.logger import Loggings
import requests
from urllib import parse
logger = Loggings()
class httprequest:
    def postform(self,url,data,headers):
        try:
            data = parse.urlencode(data)
            RequestMsg = requests.post(url=url,
                                       data=data,
                                       headers=headers,
                                       verify =False
                                       )

            return RequestMsg.json()
        except Exception as error:
            logger.info(error)

    def post(self, url, data, headers):

        try:
            RequestMsg = requests.post(url=url,
                                       data=data,
                                       headers=headers,
                                       verify=False
                                       )
            return RequestMsg.json()
        except Exception as error:
            logger.info(error)
    def get(self,url ,data,headers):
        try:
            RequestMsg = requests.get(
                url = url,
                params = data,
                headers = headers,
                verify=False
            )
            return RequestMsg.json()
        except Exception as error:
            logger.info(error)

    def delete(self,url,headers):
        try:
            Requestmsg = requests.delete(url = url,
                                         headers = headers,
                                         verify =False)
            return Requestmsg
        except Exception as error:
            logger.info(error)

    def put(self,url,data,headers):
        try:
            Requestmsg = requests.put(
                url = url,
                json = data,
                headers = headers,
                verify=False
            )
            return Requestmsg
        except Exception as error:
            logger.info(error)
