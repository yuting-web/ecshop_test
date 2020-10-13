# @Time : 2020/10/12 13:58
# @Author : 30037
# @Email : 960364395@qq.com
# @File : order_query_page.py
# @Project : test_ecshop
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from page.home_page import HomePage
from selenium.webdriver.support.select import Select
from time import sleep

"""订单查询页面"""
class OrderQueryPage(BasePage):

    input_consignee_locator = (By.ID,'consignee')
    input_phonenumber_locator = (By.ID,'mobile')
    input_adress_locator = (By.ID,'address')
    click_search_locator = (By.ID,'query')
    coutry_select_locator = (By.ID,'selCountries')
    province_select_locator = (By.ID,'selProvinces')
    city_select_locator = (By.ID,'selCities')
    district_select_locator = (By.ID,'selDistricts')











