# @Time : 2020/10/10 15:50
# @Author : 30037
# @Email : scg@gmail.com
# @File : driver.py
# @Project : test_ecshop

from selenium import webdriver

def browser_chrome():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver

def browser_firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver

def browser_ie():
    driver = webdriver.Ie()
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver
