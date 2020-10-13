# @Time : 2020/10/11 21:03
# @Author : 30037
# @Email : 960364395@qq.com
# @File : orderlist_page.py
# @Project : test_ecshop
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from page.base_page import BasePage

"""订单列表页面"""
class OrderListPage(BasePage):

    input_sn_locator = (By.ID,'order_sn')
    input_consignee_locator = (By.ID,'consignee')
    select_status_locator = (By.ID,'status')
    delete_locator = (By.ID,'btnSubmit3')
    print_locator = (By.ID,'btnSubmit4')
    click_order_locator = (By.XPATH,'//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[1]/input')
    order_number_locator = (By.XPATH,'//*[@id="order_0"]')
    consignee_locator = (By.XPATH,'//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[3]/a')
    phonenumber_locator = (By.XPATH,'//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[3]')
    adress_locator = (By.CSS_SELECTOR,'#listDiv > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(3)')
    search_locator = (By.XPATH,'/html/body/div[1]/form/input[3]')

