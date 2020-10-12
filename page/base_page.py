# @Time : 2020/10/10 15:57
# @Author : 30037
# @Email : 960364395@qq.com
# @File : base_page.py
# @Project : test_ecshop
from conf.config import LOGIN_URL
from selenium.webdriver.common.by import By

"""页面基类"""
class BasePage():
    #初始化
    def __init__(self,driver):
        self.driver = driver

    #查找元素
    def find_element(self,locator,element=None):
        if element:
            return self.find_element(*locator)
        return self.driver.find_element(*locator)

    #切换到menu-frame
    def switch_menu_frame(self):
        self.driver.switch_to.parent_frame()
        return self.driver.switch_to.frame("menu-frame")

    #切换到main-frame
    def switch_main_frame(self):
        self.driver.switch_to.parent_frame()
        return self.driver.switch_to.frame('main-frame')

    #输入数据
    def send_keys(self,locator,text):
        self.find_element(*locator).send_keys(text)

    #点击
    def click(self,locator):
        self.find_element(*locator).click()

    #退出
    def quit(self):
        self.driver.quit()



