# @Time : 2020/10/10 15:57
# @Author : 30037
# @Email : scg@gmail.com
# @File : base_page.py
# @Project : test_ecshop
from conf.config import LOGIN_URL

"""页面基类"""
class BasePage():
    #初始化
    def __init__(self,driver):
        self.driver = driver

    #打开页面
    def open(self):
        self.driver.get(LOGIN_URL)

    #查找元素
    def find_element(self,locator,element=None):
        if element:
            return self.find_element(*locator)
        return self.driver.find_element(*locator)

    #输入数据
    def send_keys(self,locator,text):
        self.find_element(*locator).send_keys(text)

    #点击
    def click(self,locator):
        self.find_element(*locator).click()

    #退出
    def quit(self):
        self.driver.quit()


