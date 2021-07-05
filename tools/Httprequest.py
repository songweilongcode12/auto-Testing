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
    def __init__(self):
        self.headers = {
            "Content-Type": "application/json; chanset=UTF-8",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"
                        }
        self.fromheaders = {
                            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"
        }
    def post(self,url,data,dataform='json'):
        try:
            if dataform == 'form':
                data = parse.urlencode(data)
                RequestMsg = requests.post(url=url,
                                           data=data,
                                           headers=self.fromheaders,
                                           verify =False
                                           )
            else:
                RequestMsg = requests.post(
                url = url,
                json = data,
                headers = self.headers,
                verify =False)
            return RequestMsg
        except Exception as error:
            logger.info(error)


    def get(self,url ,data):
        try:
            RequestMsg = requests.get(
                url = url,
                params = data,
                headers = self.headers,
                verify=False
            )

        except Exception as error:
            logger.info(error)
        else:
            return RequestMsg
    def delete(self,url):
        try:
            Requestmsg = requests.delete(url = url,
                                         headers = self.headers,
                                         verify =False)

        except Exception as error:

            logger.info(error)
        else:
            return Requestmsg
    def put(self,url,data):
        try:
            Requestmsg = requests.put(
                url = url,
                json = data,
                headers = self.headers,
                verify=False
            )

        except Exception as error:
            logger.info(error)
        else:
            return Requestmsg
