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
    search_locator = (By.XPATH,'/html/body/div[1]/form/input[3]')
    order1_locator = (By.XPATH,'//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[1]/input')
    order2_locator = (By.XPATH,'//*[@id="listDiv"]/table[1]/tbody/tr[4]/td[1]/input')
    delete_locator = (By.ID,'btnSubmit3')
    print_locator = (By.ID,'btnSubmit4')
    order_tbody_locator = (By.XPATH, '//*[@id="listDiv"]/table[1]/tbody')

    #输入订单号
    def input_sn(self,sn):
        self.find_element(self.input_sn_locator).clear()
        self.find_element(self.input_sn_locator).send_keys(sn)

    #输入收货人
    def input_consignee(self,consignee):
        self.find_element(self.input_consignee_locator).clear()
        self.find_element(self.input_consignee_locator).send_keys(consignee)

    #点击搜索按钮
    def search_click(self):
        self.find_element(self.search_locator).click()

    #选中第一个订单
    def checkbox1_click(self):
        tbody = self.find_element(By.XPATH,'//*[@id="listDiv"]/table[1]/tbody')
        tr1 = tbody.find_elements(By.TAG_NAME, 'tr')[2]
        td1 = tr1.find_elements(By.TAG_NAME, 'td')[0]
        td1.find_element(By.TAG_NAME, 'input').click()

    #打印订单
    def print_click(self):
        return self.find_element(self.print_locator).click()

    #选择订单状态
    def order_status(self):
        return self.find_element(self.select_status_locator)

    #获取订单的收货人
    def get_consignee(self):
        bp = BasePage(self.driver)
        tbody = bp.find_element(self.order_tbody_locator)
        tr = tbody.find_elements(By.TAG_NAME, 'tr')[2]
        td = tr.find_elements(By.TAG_NAME,'td')[2]
        get_consignee_name = td.find_element(By.TAG_NAME,'a').text
        return get_consignee_name

