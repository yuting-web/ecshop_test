# @Time : 2020/10/10 17:06
# @Author : 30037
# @Email : scg@gmail.com
# @File : base_case.py
# @Project : test_ecshop

import unittest
from model.driver import browser_chrome
from page.login_page import LoginPage
from time import sleep
from page.home_page import HomePage

"""用例基类"""
class BaseCase(unittest.TestCase):

    username = "admin"
    password = "admin123456"

    #实例化浏览器
    def setUp(self) -> None:
        self.driver = browser_chrome()
        sleep(1)
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for handle in handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                break
        self.driver.close()
        self.driver.switch_to.window(current_handle)
        #登录
        lp = LoginPage(self.driver)
        lp.open()
        lp.input_username(self.username)
        lp.input_password(self.password)
        lp.login_button_click()
        sleep(1)
        hp = HomePage(self.driver)
        hp.into_order()
        sleep(1)

    #关闭浏览器
    def tearDown(self) -> None:
        self.driver.quit()

