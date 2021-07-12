import unittest
from config.HTMLTestRunner.BeautifulReport import BeautifulReport
from testcases.test_login import test_login
import os
from tools.logger import Loggings
logger = Loggings()
import time

def loadtestcase():
    '''
    遍历出指定路劲下的testcase
    :return:
    '''
    testunit = unittest.TestSuite()
    testcase_path =os.path.abspath(os.path.dirname(__file__)+os.path.sep+r"../") + "/testcases/"
    logger.info("测试用例路劲为：{}".format(testcase_path))
    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
    for suit in discover:
        for case in suit:
            testunit.addTest(case)
    logger.info(testunit)
    return testunit
def runtestcaese():
    time_format = time.strftime("%Y%m%d%H%M", time.localtime())
    report_path = os.path.dirname(os.path.abspath(".")) + "/report"
    file_path = report_path + "/report" + time_format + ".html"
    file_Name = "/report" + time_format + ".html"
    logger.info(file_path)
    with open(file_path,"wb") as file:
        run = BeautifulReport(loadtestcase())
        run.report(filename= file_Name,
                   description='登录功能',
                   log_path=report_path
                   )

if __name__=='__main__':
    runtestcaese()
