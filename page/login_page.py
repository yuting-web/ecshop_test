# @Time : 2020/10/10 15:57
# @Author : 30037
# @Email : scg@gmail.com
# @File : login_page.py
# @Project : test_ecshop
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class LoginPage(BasePage):
    username_locator = (By.NAME,'username')
    password_locator = (By.NAME,'password')
    login_button_locator = (By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input')

    def input_username(self,username):
        self.find_element(self.username_locator).clear()
        self.find_element(self.username_locator).send_keys(username)

    def input_password(self,password):
        self.find_element(self.password_locator).clear()
        self.find_element(self.password_locator).send_keys(password)

    def login_button_click(self):
        self.find_element(self.login_button_locator).click()

