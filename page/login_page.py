# @Time : 2020/10/10 15:57
# @Author : 30037
# @Email : 960364395@qq.com
# @File : login_page.py
# @Project : test_ecshop
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from conf.config import LOGIN_URL

"""登录页面"""
class LoginPage(BasePage):
    username_locator = (By.NAME,'username')
    password_locator = (By.NAME,'password')
    login_button_locator = (By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input')

    #打开页面
    def open(self):
        self.driver.get(LOGIN_URL)

    #输入用户名
    def input_username(self,username):
        self.find_element(self.username_locator).clear()
        self.find_element(self.username_locator).send_keys(username)

    #输入密码
    def input_password(self,password):
        self.find_element(self.password_locator).clear()
        self.find_element(self.password_locator).send_keys(password)

    #点击登录按钮
    def login_button_click(self):
        self.find_element(self.login_button_locator).click()


