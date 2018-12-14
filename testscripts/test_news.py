# -*- coding:UTF-8 -*-
import  unittest
from time import sleep
from selenium.webdriver.common.by import By
from log_print import *
from myunit import StartEnd
from test_login import Login
from driver import *

class NewsPage(Login):
    url='/'
    def load_news_page(self):
        element=self.find_element(By.LINK_TEXT,'新闻中心')
        self.click_(element)
        sleep(2)
    def load_newspart_page(self,status):
        # status=int(status)
        elements=self.find_elements(By.LINK_TEXT,'更多>>')
        self.click_(elements[status])
        sleep(1)
        return elements
    def check_news_title(self):
        return self.title_()

class TestNewsPage(StartEnd):
    logger=get_log("test news_page")
    def test_news_page(self):
        driver=browser()
        newspage = NewsPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_news_page()
        try:
            title=newspage.check_news_title()
            self.assertEqual(title,'新闻中心 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load news page is ok")
            newspage.quit_browser_()

    def test_homenews_page(self,h_status=0):
        driver = browser()
        newspage = NewsPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_news_page()
        try:
            newspage.load_newspart_page(h_status)
            title=newspage.check_news_title()
            self.assertEqual(title,'国内新闻 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load home news page is ok")
            newspage.quit_browser_()

    def test_nationalnews_page(self, n_status=1):
        driver = browser()
        newspage = NewsPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_news_page()
        try:
            newspage.load_newspart_page(n_status)
            title = newspage.check_news_title()
            self.assertEqual(title, '国际新闻 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load nation news page is ok")
            newspage.quit_browser_()

    def test_disportnews_page(self, d_status=2):
        driver = browser()
        newspage = NewsPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_news_page()
        try:
            newspage.load_newspart_page(d_status)
            title = newspage.check_news_title()
            self.assertEqual(title, '娱乐新闻 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load disport news page is ok")
            newspage.quit_browser_()

    def test_sportnews_page(self, s_status=3):
        driver = browser()
        newspage = NewsPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_news_page()
        try:
            newspage.load_newspart_page(s_status)
            title = newspage.check_news_title()
            self.assertEqual(title, '体育新闻 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load sport news page is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

# driver=browser()
# newspage = NewsPage(driver)
# newspage.open_browser_()
# newspage.type_username()
# newspage.load_news_page()
# element=newspage.load_newspart_page()
# print(element)
# newspage.quit_browser_()