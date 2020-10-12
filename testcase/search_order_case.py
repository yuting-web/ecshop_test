# @Time : 2020/10/12 11:21
# @Author : 30037
# @Email : 960364395@qq.com
# @File : search_order_case.py
# @Project : test_ecshop
from testcase.base_case import BaseCase
from page.home_page import HomePage
from time import sleep
from page.base_page import BasePage
from page.orderlist_page import OrderListPage
from selenium.webdriver.support.select import Select

"""搜索订单"""
class SearchOrder(BaseCase):

    consignee_name = "dtt"

    #根据收货人搜索订单，用例编号（ECshop_ST_ddgl_003）
    def test_search_order_by_consignee(self):
        #进入到订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click_orderlist()
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        #输入收货人
        op = OrderListPage(self.driver)
        op.input_consignee(self.consignee_name)
        #订单状态选择最上面一项
        locator = op.order_status()
        sleep(1)
        select = Select(locator)
        select.select_by_value('-1')
        sleep(1)
        #点击搜索
        op.search_click()
        sleep(2)
        #断言
        get_consignee_name = op.get_consignee()
        self.assertEqual(self.consignee_name,get_consignee_name)