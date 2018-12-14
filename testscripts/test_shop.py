# -*- coding:UTF-8 -*-
import  unittest
from time import sleep
from selenium.webdriver.common.by import By
from log_print import *
from myunit import StartEnd
from test_login import Login
from driver import *

class ShopPage(Login):
    url='/'
    def load_master_page(self):
        element=self.find_element(By.LINK_TEXT,'网上商城')
        self.click_(element)
        sleep(2)
    def load_part_page(self,status):
        # status=int(status)
        elements=self.find_elements(By.LINK_TEXT,'更多>>')
        self.click_(elements[status])
        sleep(1)
        return elements
    def check_title(self):
        return self.title_()

class TestShopPage(StartEnd):
    logger=get_log("test shop_page")
    def test_shop_page(self):
        driver=browser()
        newspage =ShopPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            title=newspage.check_title()
            self.assertEqual(title,'网上商城 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load shop page is ok")
            newspage.quit_browser_()

    def test_digit_page(self,h_status=0):
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(h_status)
            title=newspage.check_title()
            self.assertEqual(title,'手机数码 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load digit page is ok")
            newspage.quit_browser_()

    def test_dianqi_page(self, n_status=1):
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '家用电器 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load dianqi page is ok")
            newspage.quit_browser_()

    def test_pc_page(self, d_status=2):
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(d_status)
            title = newspage.check_title()
            self.assertEqual(title, '品牌电脑 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load pc page is ok")
            newspage.quit_browser_()

    def test_book_page(self, s_status=3):
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(s_status)
            title = newspage.check_title()
            self.assertEqual(title, '图书杂志 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load book page is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

