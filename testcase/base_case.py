# @Time : 2020/10/10 17:06
# @Author : 30037
# @Email : scg@gmail.com
# @File : base_case.py
# @Project : test_ecshop

import unittest
from model.driver import browser_chrome

"""用例基类"""
class BaseCase(unittest.TestCase):
    #实例化浏览器
    def setUp(self) -> None:
        self.driver = browser_chrome()
    #关闭浏览器
    def tearDown(self) -> None:
        self.driver.quit()

