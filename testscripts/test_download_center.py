# -*- coding:UTF-8 -*-
import  unittest
from time import sleep
from selenium.webdriver.common.by import By
from log_print import *
# from testdata import *
from myunit import StartEnd
from test_login import Login
from driver import *

class DownloadPage(Login):
    url='/'
    def load_master_page(self):
        element=self.find_element(By.LINK_TEXT,'下载中心')
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

class TestDownloadPage(StartEnd):
    logger=get_log("test download_page")
    def test_download_page(self):
        driver=browser()
        newspage =DownloadPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            title=newspage.check_title()
            self.assertEqual(title,'下载中心 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load download page is ok")
            newspage.quit_browser_()

    def test_sys_page(self,h_status=0):
        driver = browser()
        newspage = DownloadPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(h_status)
            title=newspage.check_title()
            self.assertEqual(title,'系统软件 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load sys news page is ok")
            newspage.quit_browser_()

    def test_nettools_page(self, n_status=1):
        driver = browser()
        newspage = DownloadPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '网络工具 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load nettools page is ok")
            newspage.quit_browser_()

    def test_safetools_page(self, d_status=2):
        driver = browser()
        newspage = DownloadPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(d_status)
            title = newspage.check_title()
            self.assertEqual(title, '安全相关 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load safetools news page is ok")
            newspage.quit_browser_()

    def test_mediatools_page(self, s_status=3):
        driver = browser()
        newspage = DownloadPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(s_status)
            title = newspage.check_title()
            self.assertEqual(title, '媒体工具 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load sport news page is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

