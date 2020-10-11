# @Time : 2020/10/11 15:31
# @Author : 30037
# @Email : 960364395@qq.com
# @File : into_main-frame_page.py
# @Project : test_ecshop
from page.login_page import LoginPage
from page.home_page import HomePage
from testcase.base_case import BaseCase
import unittest
from time import sleep

class IntoMainframe(BaseCase):

    username = "admin"
    password = "admin123456"

    #登录ecshop
    def test_orderlist(self):
        lp = LoginPage(self.driver)
        lp.open()
        lp.input_username(self.username)
        lp.input_password(self.password)
        lp.login_button_click()
        sleep(2)

        hp = HomePage(self.driver)
        hp.into_order()
        sleep(3)

if __name__ == '__main__':
    unittest.main()


