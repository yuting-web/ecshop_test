# @Time : 2020/10/12 22:28
# @Author : 30037
# @Email : 960364395@qq.com
# @File : delete_case.py
# @Project : test_ecshop

from page.orderlist_page import OrderListPage
from page.home_page import HomePage
from testcase.base_case import BaseCase
from time import sleep
from selenium.webdriver.common.by import By
from page.base_page import BasePage

"""删除订单"""
class DeleteCase(BaseCase):

    order_tbody_locator = (By.XPATH, '//*[@id="listDiv"]/table[1]/tbody')

    #成功删除订单
    def test_delete_case(self):
        #进入订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click_orderlist()
        sleep(1)
        #切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        #选中订单
        op = OrderListPage(self.driver)
        tbody = op.find_element(self.order_tbody_locator)
        tr1 = tbody.find_elements(By.TAG_NAME, 'tr')[2]
        td1 = tr1.find_elements(By.TAG_NAME, 'td')[0]
        td1.find_element(By.TAG_NAME, 'input').click()
        sleep(1)
        get_order_number = self.driver.find_element(By.XPATH,'//*[@id="order_0"]').text
        #点击删除
        op =  OrderListPage(self.driver)
        op.click_delete()
        sleep(1)
        #弹出框点击确认删除
        self.driver.switch_to.alert.accept()
        sleep(6)
        get_order_number1 = self.driver.find_element(By.XPATH,'//*[@id="order_0"]').text
        #断言
        self.assertNotEqual(get_order_number,get_order_number1)

    #取消删除订单
    def test_delete_cancel(self):
        #进入订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click_orderlist()
        sleep(1)
        #切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        #选中订单
        op = OrderListPage(self.driver)
        tbody = op.find_element(self.order_tbody_locator)
        tr1 = tbody.find_elements(By.TAG_NAME, 'tr')[2]
        td1 = tr1.find_elements(By.TAG_NAME, 'td')[0]
        td1.find_element(By.TAG_NAME, 'input').click()
        sleep(1)
        get_order_number = self.driver.find_element(By.XPATH,'//*[@id="order_0"]').text
        #点击删除
        op =  OrderListPage(self.driver)
        op.click_delete()
        sleep(1)
        #弹出框点击取消删除
        self.driver.switch_to.alert.dismiss()
        sleep(6)
        get_order_number1 = self.driver.find_element(By.XPATH,'//*[@id="order_0"]').text
        #断言
        self.assertEqual(get_order_number,get_order_number1)


