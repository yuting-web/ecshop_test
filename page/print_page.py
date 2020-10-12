# @Time : 2020/10/12 9:58
# @Author : 30037
# @Email : 960364395@qq.com
# @File : print_page.py
# @Project : test_ecshop
from page.base_page import BasePage
from selenium.webdriver.common.by import By

"""打印订单页面"""
class PrintPage(BasePage):

    printorder_word_locator = (By.CSS_SELECTOR,'body > h1')

    #获取“订单信息”字样
    def get_orderinformation_word(self):
        element = self.find_element(self.printorder_word_locator)
        ele = element.text
        return ele

