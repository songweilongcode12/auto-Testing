import sys
sys.path.append('./../../auto-Testing/')
import unittest
from config.HTMLTestRunner.BeautifulReport import BeautifulReport
from config.HTMLTestRunner.HTMLTestReportCN import HTMLTestRunner
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
    testcase_path = os.path.dirname(os.path.abspath("."))+ "/testcases/"
    # logger.info(testcase_path)
    discover = unittest.defaultTestLoader.discover(testcase_path,pattern="test_*.py")
    for suit in discover:
        for case in suit:
            testunit.addTest(case)
    # logger.info(testunit)
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

def runall():
    suit = unittest.TestSuite()
    loader = unittest.TestLoader()
    suit.addTest(loader.loadTestsFromTestCase(test_login))
    time_format = time.strftime("%Y%m%d%H%M", time.localtime())
    report_path = os.path.dirname(os.path.abspath(".")) + "/report"
    file_path = report_path + "/report" + time_format + ".html"
    with open(file_path,'wb') as file:
        runner = HTMLTestRunner(
            stream=file,
            title='登录功能',
            description='验证成功登录场景',
            tester='admin'
        )
        runner.run(suit)

if __name__=='__main__':
    runtestcaese()
