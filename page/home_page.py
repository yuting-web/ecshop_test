# @Time : 2020/10/10 17:17
# @Author : 30037
# @Email : 960364395@qq.com
# @File : home_page.py
# @Project : test_ecshop
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class HomePage(BasePage):

    order_locator = (By.XPATH,'//*[@id="menu-ul"]/li[3]')
    orderlist_locator = (By.XPATH, '//*[@id="menu-ul"]/li[3]/ul/li[1]/a')

    #进入订单界面
    def into_order(self):
        self.switch_main_frame()
        sleep(1)
        self.find_element(self.order_locator).click()
        sleep(1)
        self.find_element(self.orderlist_locator).click()
        sleep(3)






