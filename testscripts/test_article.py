# -*- coding:UTF-8 -*-
import  unittest
from time import sleep
from selenium.webdriver.common.by import By
from log_print import *
from myunit import StartEnd
from test_login import Login
from driver import *

class ArticlePage(Login):
    url='/'
    def load_master_page(self):
        element=self.find_element(By.LINK_TEXT,'文章中心')
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

class TestArticlePage(StartEnd):
    logger=get_log("test Articl_page")
    def test_article_page(self):
        driver=browser()
        newspage =ArticlePage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            title=newspage.check_title()
            self.assertEqual(title,'文章中心 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load article page is ok")
            newspage.quit_browser_()

    def test_novel_page(self,h_status=0):
        driver = browser()
        newspage = ArticlePage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(h_status)
            title=newspage.check_title()
            self.assertEqual(title,'小说 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load novel page is ok")
            newspage.quit_browser_()

    def test_porse_page(self, n_status=1):
        driver = browser()
        newspage = ArticlePage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '散文 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load porse page is ok")
            newspage.quit_browser_()

    def test_portry_page(self, n_status=2):
        driver = browser()
        newspage = ArticlePage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '诗歌 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load poetry page is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

