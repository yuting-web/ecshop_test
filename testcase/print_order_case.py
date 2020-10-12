# @Time : 2020/10/11 22:51
# @Author : 30037
# @Email : 960364395@qq.com
# @File : print-order.py
# @Project : test_ecshop
from testcase.base_case import BaseCase
from page.orderlist_page import OrderListPage
from page.home_page import HomePage
from selenium.webdriver.common.by import By
from time import sleep
from page.base_page import BasePage
from page.print_page import PrintPage

"""打印订单"""
class printOrder(BaseCase):

    order_tbody_locator = (By.XPATH, '//*[@id="listDiv"]/table[1]/tbody')
    assert_word = "订单信息"
    #打印订单，用例编号（ECshop_ST_ddgl_008）
    def test_print_order(self):
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
        #点击打印订单
        op.print_click()
        sleep(1)
        #切换到新开窗口订单打印界面
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for handle in handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                break
        #断言
        pp = PrintPage(self.driver)
        get_word = pp.get_orderinformation_word()
        self.assertEqual(self.assert_word,get_word)

