# @Time : 2020/10/10 15:57
# @Author : 30037
# @Email : 960364395@qq.com
# @File : login_page.py
# @Project : test_ecshop
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from conf.config import LOGIN_URL
from selenium.webdriver.remote.webelement import WebElement

"""登录页面"""
class LoginPage(BasePage):
    username_locator = (By.NAME,'username')
    password_locator = (By.NAME,'password')
    login_button_locator = (By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input')
    username = 'admin'
    password = 'admin123456'

    # 登录获取cookie
    def get_cookie(self):
        bp = BasePage(self.driver)
        lp = LoginPage(self.driver)
        bp.open(LOGIN_URL)
        self.send_keys(self.username_locator,self.username)
        self.send_keys(self.password_locator,self.password)
        self.click(self.login_button_locator)
        data = self.driver.get_cookies()[0]
        data = str(data)
        f = open('./cookie', "w")
        f.write(data)
        f.close()


    def read_new_cookie(self):
        """读取cookie"""
        with open(r'C:\Users\30037\PycharmProjects\test_ecshop\cookie', "r") as f:
            a = f.readline()
            cookie = eval(a)
            return cookie

    def add_cookie(self, cookie):
        """浏览器添加cookie"""
        self.driver.get("http://192.168.1.164")
        self.driver.add_cookie(cookie)
    #
    #
    #
