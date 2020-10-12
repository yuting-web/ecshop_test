# @Time : 2020/10/10 17:17
# @Author : 30037
# @Email : 960364395@qq.com
# @File : home_page.py
# @Project : test_ecshop
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

"""主页面"""
class HomePage(BasePage):

    order_manage_locator = (By.XPATH,'//*[@id="menu-ul"]/li[3]')
    orderlist_locator = (By.XPATH, '//*[@id="menu-ul"]/li[3]/ul/li[1]/a')
    order_qurey_locator = (By.XPATH, '//*[@id="menu-ul"]/li[3]/ul/li[2]/a')

    #点击订单管理
    def into_order(self):
        self.switch_menu_frame()
        sleep(1)
        return  self.find_element(self.order_manage_locator).click()

    #点击订单列表
    def click_orderlist(self):
        return self.find_element(self.orderlist_locator).click()

    #点击订单查询
    def click_order_query(self):
        return self.find_element(self.order_qurey_locator).click()









