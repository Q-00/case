import unittest
from excelUtil.excelFile import ExcelFile
from requestUtil.requests import RequestUtil
from logUtil.log import loggr

class DoCase(unittest.TestCase):
    def setUp(self):
        self.log = loggr.log(self)
        self.excelFile = ExcelFile(url='C:/Users/Qing/Desktop/test.xls')
        self.request = RequestUtil()

    def testOne(self):
        self.log.info('-------testOne start----------')
        method = self.excelFile.ReadData(0, 0)
        url = self.excelFile.ReadData(0, 1)
        data = self.excelFile.ReadData(0, 2)
        header = self.excelFile.ReadData(0, 3)

        result = self.request.DoRequest(method=method, url=url, data=eval(data),header=None)
        self.log.info('-------'+result['resultcode'])
        self.assertEqual('200',result['resultcode'])
        # self.excelFile.writeResult(0, 4, actualResult)

    # def tearDown(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
    # unittest.TestCase()
    # Load = unittest.TestLoader()
    # unittest.TestRunner()
    # unittest.TestSuite()
    # unittest.load_tests()