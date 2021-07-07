#!/usr/bin/python
# -*- coding=utf-8 -*-
# author : Lenovo
# date: 2021/6/17 10:23
# version: 0.1
import os
import time
from loguru import logger

# log_path = os.path.abspath(os.path.dirname(__file__) + os.path.sep + "../") + '/log/' + time.strftime("%Y-%m-%d") + '.log'

class Loggings:
    log_path = os.path.abspath(os.path.dirname(__file__) + os.path.sep + "../") + '/log/' + time.strftime(
        "%Y-%m-%d") + '.log'
    __instance = None
    logger.add(log_path,
               rotation="50MB",
               encoding="utf-8",
               enqueue=True,
               retention="10 days")

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    @staticmethod
    def info(msg):
        return logger.info(msg)

    @staticmethod
    def debug(msg):
        return logger.debug(msg)

    @staticmethod
    def warning(msg):
        return logger.warning(msg)

    @staticmethod
    def error(msg):
        return logger.error(msg)

