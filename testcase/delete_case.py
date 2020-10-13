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

    #成功删除订单，用例编号：ECshop_ST_ddgl_006
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
        op.click(op.click_order_locator)
        get_order_number = op.text(op.order_number_locator)
        #点击删除
        op.click(op.delete_locator)
        sleep(1)
        #弹出框点击确认删除
        self.driver.switch_to.alert.accept()
        sleep(4)
        get_order_number1 = op.text(op.order_number_locator)
        #断言
        self.assertNotEqual(get_order_number,get_order_number1)

    #取消删除订单，用例编号：ECshop_ST_ddgl_007
    def test_delete_case_cancelself(self):
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
        op.click(op.click_order_locator)
        get_order_number = op.text(op.order_number_locator)
        #点击删除
        op.click(op.delete_locator)
        sleep(1)
        #弹出框点击确认删除
        self.driver.switch_to.alert.dismiss()
        sleep(4)
        get_order_number1 = op.text(op.order_number_locator)
        #断言
        self.assertEqual(get_order_number,get_order_number1)

