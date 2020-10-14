# @Time : 2020/10/10 17:06
# @Author : 30037
# @Email : scg@gmail.com
# @File : base_case.py
# @Project : test_ecshop

import unittest
from model.driver import browser_chrome
from page.login_page import LoginPage
from time import sleep
from page.home_page import HomePage
from conf.config import LOGIN_URL

"""用例基类"""
class BaseCase(unittest.TestCase):

    username = "admin"
    password = "admin123456"

    #实例化浏览器
    def setUp(self) -> None:
        self.driver = browser_chrome()
        sleep(1)
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for handle in handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                break
        self.driver.close()
        self.driver.switch_to.window(current_handle)
        lp = LoginPage(self.driver)
        cookie = lp.read_new_cookie()
        lp.add_cookie(cookie)
        self.driver.get(LOGIN_URL)
        hp = HomePage(self.driver)
        hp.into_order()
        sleep(1)

    #关闭浏览器
    def tearDown(self) -> None:
        self.driver.quit()

    # #切换并进入到订单列表
    # def into_orderlist(self):
    #     #进入订单页面
    #     hp = HomePage(self.driver)
    #     sleep(1)
    #     hp.click(hp.orderlist_locator)
    #     sleep(1)
    #     #切换到main-frame
    #     bp = BasePage(self.driver)
    #     bp.switch_main_frame()
    #     sleep(1)
