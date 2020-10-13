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
from page.order_query_page import OrderQueryPage
from selenium.webdriver.common.by import By
import unittest
from page.orderlist_page import OrderListPage

"""搜索订单"""
class SearchOrder(BaseCase):

    consignee_name = "dtt"
    phonenumber = "15342601420"
    adress_assert = '海德'
    lookover_locator = (By.XPATH,'//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]/a')
    assert_adress_locator = (By.XPATH,'/html/body/form/div[1]/table/tbody/tr[18]/td[2]')
    assert_adress = '东城区'


    #根据收货人搜索订单，用例编号（ECshop_ST_ddgl_003）
    def test_search_order_by_consignee(self):
        #进入到订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click(hp.orderlist_locator)
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        #输入收货人
        op = OrderListPage(self.driver)
        op.send_keys(op.input_consignee_locator,self.consignee_name)
        #订单状态选择最上面一项
        select = op.select(op.select_status_locator)
        select.select_by_value('-1')
        sleep(1)
        #点击搜索
        op.click(op.search_locator)
        sleep(1)
        #断言
        get_consignee_name = op.text(op.consignee_locator)
        self.assertEqual(self.consignee_name,get_consignee_name)

    #根据手机号码搜索订单，用例编号“ECshop_ST_ddgl_016”
    def test_search_order_by_phonenumber(self):
        # 进入到订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click(hp.order_qurey_locator)
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        # 输入收手机号码
        oqp = OrderQueryPage(self.driver)
        hp.send_keys(oqp.input_phonenumber_locator,self.phonenumber)
        # 点击搜索
        hp.click(oqp.click_search_locator)
        sleep(1)
        #断言
        op = OrderListPage(self.driver)
        text = hp.text(op.phonenumber_locator)
        self.assertIn(self.phonenumber,text)

    #通过地址查询订单，用例编号，ECshop_ST_ddgl_014
    def test_search_order_by_adress(self):
        hp = HomePage(self.driver)
        sleep(1)
        hp.click(hp.order_qurey_locator)
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        # 输入地址
        oqp = OrderQueryPage(self.driver)
        hp.send_keys(oqp.input_adress_locator,self.adress_assert)
        # 点击搜索
        hp.click(oqp.click_search_locator)
        sleep(1)
        #断言
        op = OrderListPage(self.driver)
        text = hp.text(op.adress_locator)
        self.assertIn(self.adress_assert,text)

    #根据收货人查询订单，用例编号：ECshop_ST_ddgl_012
    def test_search_order_by_consignee_query(self):
        hp = HomePage(self.driver)
        sleep(1)
        hp.click(hp.order_qurey_locator)
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        # 输入收货人
        oqp = OrderQueryPage(self.driver)
        hp.send_keys(oqp.input_consignee_locator,self.consignee_name)
        # 点击搜索
        hp.click(oqp.click_search_locator)
        sleep(1)
        #断言
        op = OrderListPage(self.driver)
        text = hp.text(op.consignee_locator)
        self.assertIn(self.consignee_name,text)

    #根据所在地区查找订单
    def test_search_order_by_area(self):
        hp = HomePage(self.driver)
        sleep(1)
        hp.click(hp.order_qurey_locator)
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        # 选择地区
        oqp = OrderQueryPage(self.driver)
        hp.select(oqp.coutry_select_locator).select_by_index(1)
        sleep(1)
        hp.select(oqp.province_select_locator).select_by_index(1)
        sleep(1)
        hp.select(oqp.city_select_locator).select_by_index(1)
        sleep(1)
        hp.select(oqp.district_select_locator).select_by_index(1)
        sleep(1)
        # 点击搜索
        hp.click(oqp.click_search_locator)
        sleep(1)
        #断言
        hp.click(self.lookover_locator)
        sleep(1)
        text = hp.text(self.assert_adress_locator)
        self.assertIn(self.assert_adress,text)


if __name__ == '__main__':
    unittest.main()



