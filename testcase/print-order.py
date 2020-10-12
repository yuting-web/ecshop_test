# @Time : 2020/10/11 22:51
# @Author : 30037
# @Email : 960364395@qq.com
# @File : print-order.py
# @Project : test_ecshop
from testcase.base_case import BaseCase
from page.orderlist_page import orderlist_page
from page.home_page import HomePage
from selenium.webdriver.common.by import By
from time import sleep
from page.base_page import BasePage

"""打印订单"""
class printOrder(BaseCase):

    order_tbody_locator = (By.XPATH, '//*[@id="listDiv"]/table[1]/tbody')
    #进入订单列表
    def test_print_order(self):
        hp = HomePage(self.driver)
        sleep(1)
        hp.click_orderlist()
        sleep(1)
    #点击订单
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        op = orderlist_page(self.driver)
        tbody = op.find_element(self.order_tbody_locator)
        tr1 = tbody.find_elements(By.TAG_NAME, 'tr')[2]
        td1 = tr1.find_elements(By.TAG_NAME, 'td')[0]
        td1.find_element(By.TAG_NAME, 'input').click()
        sleep(1)
    #点击打印订单
        op.print_click()
        sleep(1)

    #断言
