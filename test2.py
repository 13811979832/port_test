# _*_ coding: utf-8 _*_
__author__ = 'butr'
__date__ = '18/9/10 上午10:59'

import unittest
import requests
import json

class TesApi(unittest.TestCase):
    def setUp(self):
        print("init by setUp...")

    def tearDown(self):
        print("end bu tearDown...")


    def test_file(self):
        with open("test.txt", 'r', encoding='utf-8',errors="ignore") as f:
            count = len(open('test.txt', 'r').readlines())
            for i in range(count):
                for line in f.readlines():
                    print(line.strip())
                    res = requests.get(line.strip())
                    print(res.status_code)

    
if __name__ == "__main__":
    # unittest.main()
    #装载测试用例
    test_cases = unittest.TestLoader().loadTestsFromTestCase(TesApi)
    #使用测试套件并打包测试用例
    test_suit = unittest.TestSuite()
    test_suit.addTests(test_cases)
    #运行测试套件，并返回测试结果
    test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
    


































