# @Time : 2020/10/11 17:41
# @Author : 30037
# @Email : 960364395@qq.com
# @File : xainxing.py
# @Project : test_ecshop

from selenium import webdriver
from page.home_page import HomePage
from time import sleep
from page.base_page import BasePage
from page.order_query_page import OrderQueryPage
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://192.168.1.164/upload/admin")
driver.maximize_window()
driver.find_element(By.NAME,'username').send_keys('admin')
driver.find_element(By.NAME,'password').send_keys('admin123456')
driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/input').click()
driver.switch_to.parent_frame()
driver.switch_to.frame("menu-frame")
sleep(1)
driver.find_element(By.XPATH,'//*[@id="menu-ul"]/li[3]').click()
sleep(2)
# # driver.find_element(By.XPATH,'//*[@id="menu-ul"]/li[3]/ul/li[1]/a').click()
# # sleep(2)
# driver.find_element(By.XPATH, '//*[@id="menu-ul"]/li[3]/ul/li[2]/a').click()
# driver.switch_to.parent_frame()
# driver.switch_to.frame('main-frame')
# sleep(1)
# tbody = driver.find_element(By.XPATH,'/html/body/div[1]/form/table/tbody')
# # tr = tbody.find_elements(By.TAG_NAME,'tr')[3]
# # td = tr.find_elements(By.TAG_NAME,'td')[1]
# # td.find_element(By.TAG_NAME,'input').send_keys('海德')
#
# tr = tbody.find_elements(By.TAG_NAME, 'tr')[5]
# td = tr.find_elements(By.TAG_NAME, 'td')[1]
#
# select_country = td.find_elements(By.TAG_NAME,'select')[0]
# select_province = td.find_elements(By.TAG_NAME,'select')[1]
# select_city = td.find_elements(By.TAG_NAME,'select')[2]
# Select(select_country).select_by_index(1)
# sleep(1)
# Select(select_province).select_by_index(1)
# sleep(1)
# Select(select_city).select_by_index(1)
# sleep(2)
# tr2 = tbody.find_elements(By.TAG_NAME,'tr')[9]
# td2 = tr2.find_elements(By.TAG_NAME,'td')[0]
# input = td2.find_elements(By.TAG_NAME,'input')[0]
# input.click()
# sleep(2)
# tbody = driver.find_element(By.XPATH,'//*[@id="listDiv"]/table[1]/tbody')
# tr1 = tbody.find_elements(By.TAG_NAME,'tr')[2]
# td1 = tr1.find_elements(By.TAG_NAME,'td')[0]
# td1.find_element(By.TAG_NAME,'input').click()

# tr = tbody.find_elements(By.TAG_NAME, 'tr')[2]
# td = tr.find_elements(By.TAG_NAME, 'td')[2]
# get_consignee_name = td.find_element(By.TAG_NAME, 'a').text
# print(get_consignee_name)
# sleep(3)


# handles = driver.window_handles
# current_handle = driver.current_window_handle
# print(handles)
# print(current_handle)
# driver.switch_to.window(handles[1])
# sleep(2)
# driver.close()
# driver.switch_to.window(current_handle)
# sleep(2)

hp = HomePage(driver)
sleep(1)
hp.click_order_query()
sleep(1)
# 切换到main-frame
bp = BasePage(driver)
bp.switch_main_frame()
sleep(1)
# 输入收货人
op = OrderQueryPage(driver)
op.input_consignee('dtt')
# 点击搜索
tbody_locator = (By.XPATH, '/html/body/div[1]/form/table/tbody')
tbody = bp.find_element(tbody_locator)
tr2 = tbody.find_elements(By.TAG_NAME, 'tr')[9]
td2 = tr2.find_elements(By.TAG_NAME, 'td')[0]
input = td2.find_elements(By.TAG_NAME, 'input')[0]
input.click()
sleep(2)
# 断言
bp.switch_menu_frame()
bp.switch_main_frame()
tbody1 = driver.find_element(By.XPATH,'//*[@id="listDiv"]/table[1]/tbody')
print('bbbbbb')
tr1 = tbody1.find_elements(By.TAG_NAME,'tr')[2]
print('aaaaa')
td1 = tr1.find_elements(By.TAG_NAME,'td')[2]
print('-----')
aa = td1.find_elements(By.TAG_NAME,'a')[0]
print(aa.text)



driver.quit()