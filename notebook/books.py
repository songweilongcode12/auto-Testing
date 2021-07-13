import json

from ddt import ddt,data,unpack
import unittest
from tools.logger import Loggings
logger = Loggings()
from  tools.excel_util import excel_util
from Module.login import login
import requests
@ddt
class testcase(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    filepath = r'D:\TestFiles\project\auto-Testing\data\logindata.xlsx'
    excel = excel_util(filepath,sheetName='Sheet1')
    testdata = excel.next()
    logger.info(testdata)

    @data(*testdata)
    def test_01(self,testdata):
        data = json.loads(testdata['data'])
        headers = json.loads(testdata['headers'])
        url = testdata['url']
        runner = login()
        result = runner.login_success(
            url=url,
            data=data,
            headers=headers
        )



if __name__ == '__main__':
    unittest.main()
