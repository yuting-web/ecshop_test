# @Time : 2020/10/10 15:57
# @Author : 30037
# @Email : 960364395@qq.com
# @File : base_page.py
# @Project : test_ecshop
from conf.config import LOGIN_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement

"""页面基类"""
class BasePage():
    #初始化
    def __init__(self,driver):
        self.driver = driver

    #查找单个元素
    def find_element(self,locator,element=None):
        if element and isinstance(element,WebElement):
            return self.find_element(*locator)
        return self.driver.find_element(*locator)

    # 查找元素列表
    def find_elements(self, locator, elements=None):
        if elements and isinstance(elements, WebElement):
            return self.find_elements(*locator)
        return self.driver.find_elements(*locator)

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
        self.find_element(locator).send_keys(text)

    #点击
    def click(self,locator):
        self.find_element(locator).click()

    #退出
    def quit(self):
        self.driver.quit()

    #切换窗口
    def switch_window(self):
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for handle in handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                break

    #获取文本
    def text(self,locator):
        return self.find_element(locator).text

    #select类
    def select(self,locator):
        element = self.find_element(locator)
        return Select(element)

    def open(self,url):
        self.driver.get(url)




