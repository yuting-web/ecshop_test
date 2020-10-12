# @Time : 2020/10/12 13:58
# @Author : 30037
# @Email : 960364395@qq.com
# @File : order_select_page.py
# @Project : test_ecshop
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from page.home_page import HomePage
from selenium.webdriver.support.select import Select
from time import sleep

"""订单查询页面"""
class OrderQueryPage(BasePage):

    tbody_locator = (By.XPATH,'/html/body/div[1]/form/table/tbody')
    order_tbody_locator = (By.XPATH, '//*[@id="listDiv"]/table[1]/tbody')

    #输入收货人
    def input_consignee(self,consignee):
        tbody = self.find_element(self.tbody_locator)
        tr = tbody.find_elements(By.TAG_NAME,'tr')[2]
        td = tr.find_elements(By.TAG_NAME,'td')[3]
        td.find_element(By.TAG_NAME,'input').send_keys(consignee)

    #输入手机号
    def input_phonenumber(self,phonenumber):
        tbody = self.find_element(self.tbody_locator)
        tr = tbody.find_elements(By.TAG_NAME,'tr')[4]
        td = tr.find_elements(By.TAG_NAME,'td')[3]
        td.find_element(By.TAG_NAME,'input').send_keys(phonenumber)

    #输入地址
    def input_adress(self,adress):
        tbody = self.find_element(self.tbody_locator)
        tr = tbody.find_elements(By.TAG_NAME,'tr')[3]
        td = tr.find_elements(By.TAG_NAME,'td')[1]
        td.find_element(By.TAG_NAME,'input').send_keys(adress)

    #选择所在地区
    def select_address(self):
        tbody = self.find_element(self.tbody_locator)
        tr = tbody.find_elements(By.TAG_NAME,'tr')[5]
        td = tr.find_elements(By.TAG_NAME,'td')[1]
        select_country = td.find_elements(By.TAG_NAME,'select')[0]
        select_province = td.find_elements(By.TAG_NAME,'select')[1]
        select_city = td.find_elements(By.TAG_NAME,'select')[2]
        select_area = td.find_elements(By.TAG_NAME,'select')[3]
        Select(select_country).select_by_index(1)
        sleep(1)
        Select(select_province).select_by_index(1)
        sleep(1)
        Select(select_city).select_by_index(1)
        sleep(1)
        Select(select_area).select_by_index(1)

    #获取订单的收货人
    def get_consignee(self):
        bp = BasePage(self.driver)
        tbody = bp.find_element(self.order_tbody_locator)
        tr = tbody.find_elements(By.TAG_NAME, 'tr')[2]
        td = tr.find_elements(By.TAG_NAME,'td')[2]
        get_consignee_name = td.find_element(By.TAG_NAME,'a').text
        return get_consignee_name










