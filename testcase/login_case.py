# @Time : 2020/10/10 17:03
# @Author : 30037
# @Email : 960364395@qq.com
# @File : login_case.py
# @Project : test_ecshop
from testcase.base_case import BaseCase
from page.login_page import LoginPage
from time import sleep

"""登录测试"""
class LoginTest(BaseCase):

    username = "admin"
    password = "admin123456"
    #登录ecshop
    def test_login(self):
        lp = LoginPage(self.driver)
        lp.open()
        lp.input_username(self.username)
        lp.input_password(self.password)
        lp.login_button_click()


