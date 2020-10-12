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
from page.order_select_page import OrderQueryPage
from selenium.webdriver.common.by import By
import unittest

"""搜索订单"""
class SearchOrder(BaseCase):

    consignee_name = "dtt"
    phonenumber = "15342601420"
    tbody_locator = (By.XPATH, '/html/body/div[1]/form/table/tbody')
    tbody1_locator = (By.CSS_SELECTOR,'#listDiv > table:nth-child(1) > tbody')
    tr_locator = (By.TAG_NAME, 'tr')
    td_locator = (By.TAG_NAME, 'td')
    a_locator = (By.TAG_NAME, 'a')
    tbody2_locator = (By.XPATH, '/html/body/form/div[1]/table/tbody')


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
        sleep(1)
        #断言
        get_consignee_name = op.get_consignee()
        self.assertEqual(self.consignee_name,get_consignee_name)

    #根据手机号码搜索订单，用例编号“ECshop_ST_ddgl_016”
    def test_search_order_by_phonenumber(self):
        # 进入到订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click_order_query()
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        # 输入收手机号码
        oqp = OrderQueryPage(self.driver)
        oqp.input_phonenumber(self.phonenumber)
        # 点击搜索
        tbody = bp.find_element(self.tbody_locator)
        tr2 = tbody.find_elements(By.TAG_NAME, 'tr')[9]
        td2 = tr2.find_elements(By.TAG_NAME, 'td')[0]
        input = td2.find_elements(By.TAG_NAME, 'input')[0]
        input.click()
        sleep(1)
        #断言
        tbody1 = bp.find_element(self.tbody1_locator)
        tr = tbody1.find_elements(*self.tr_locator)[2]
        td = tr.find_elements(*self.td_locator)[2]
        self.assertEqual(td.find_elements(*self.a_locator)[0].text,'15342601420')

    #通过地址查询订单，用例编号，ECshop_ST_ddgl_014
    def test_search_order_by_adress(self):
        # 进入到订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click_order_query()
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        # 输入地址
        oqp = OrderQueryPage(self.driver)
        oqp.input_adress('海德')
        # 点击搜索
        tbody = bp.find_element(self.tbody_locator)
        tr2 = tbody.find_elements(By.TAG_NAME, 'tr')[9]
        td2 = tr2.find_elements(By.TAG_NAME, 'td')[0]
        input = td2.find_elements(By.TAG_NAME, 'input')[0]
        input.click()
        sleep(1)
        #断言
        tbody1 = bp.find_element(self.tbody1_locator)
        tr = tbody1.find_elements(*self.tr_locator)[2]
        td = tr.find_elements(*self.td_locator)[2]
        x = td.text.strip().strip("dtt [TEL: 15342601420]").strip("\n")
        self.assertEqual(x,'海德')

    #根据收货人查询订单，用例编号：ECshop_ST_ddgl_012
    def test_search_order_by_consignee2(self):
        # 进入到订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click_order_query()
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        # 输入地址
        oqp = OrderQueryPage(self.driver)
        oqp.input_consignee('dtt')
        # 点击搜索
        tbody = bp.find_element(self.tbody_locator)
        tr2 = tbody.find_elements(By.TAG_NAME, 'tr')[9]
        td2 = tr2.find_elements(By.TAG_NAME, 'td')[0]
        input = td2.find_elements(By.TAG_NAME, 'input')[0]
        input.click()
        sleep(1)
        # 断言
        get_consignee_name = oqp.get_consignee()
        self.assertEqual(self.consignee_name,get_consignee_name)

    #根据所在地区查找订单
    def test_search_order_by_area(self):
        # 进入到订单页面
        hp = HomePage(self.driver)
        sleep(1)
        hp.click_order_query()
        sleep(1)
        # 切换到main-frame
        bp = BasePage(self.driver)
        bp.switch_main_frame()
        sleep(1)
        # 输入地址
        oqp = OrderQueryPage(self.driver)
        oqp.select_address()
        # 点击搜索
        tbody = bp.find_element(self.tbody_locator)
        tr2 = tbody.find_elements(By.TAG_NAME, 'tr')[9]
        td2 = tr2.find_elements(By.TAG_NAME, 'td')[0]
        input = td2.find_elements(By.TAG_NAME, 'input')[0]
        input.click()
        sleep(1)
        # 断言
        # olp = OrderListPage(self.driver)
        # olp.lookover_order()
        self.driver.find_element(By.XPATH,'//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[7]/a').click()
        sleep(1)
        tbody2 = bp.find_element(self.tbody2_locator)
        tr = tbody2.find_elements(By.TAG_NAME,'tr')[17]
        td = tr.find_elements(By.TAG_NAME,'td')[1]
        get_area = td.text.strip("海德").strip().strip('[').strip(']').split(" ")[3]
        self.assertEqual(get_area,'东城区')


if __name__ == '__main__':
    unittest.main()



