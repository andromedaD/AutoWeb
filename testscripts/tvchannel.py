# -*- coding:UTF-8 -*-
import  unittest
from time import sleep
from selenium.webdriver.common.by import By
from log_print import *
from myunit import StartEnd
from test_login import Login
from driver import *

class TvchannelPage(Login):
    url='/'
    def load_master_page(self):
        element=self.find_element(By.LINK_TEXT,'影视频道')
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

class TestTvchannelPage(StartEnd):
    logger=get_log("test tvchannel_page")
    def test_tvchannel_page(self):
        driver=browser()
        newspage =TvchannelPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            title=newspage.check_title()
            self.assertEqual(title,'影视频道 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load tvchannel page is ok")
            newspage.quit_browser_()

    def test_actionvideo_page(self,h_status=0):
        driver = browser()
        newspage = TvchannelPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(h_status)
            title=newspage.check_title()
            self.assertEqual(title,'动作片 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load action video page is ok")
            newspage.quit_browser_()

    def test_lovevideo_page(self, n_status=1):
        driver = browser()
        newspage = TvchannelPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '爱情片 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load lovevideo page is ok")
            newspage.quit_browser_()

    def test_comedy_page(self, d_status=2):
        driver = browser()
        newspage = TvchannelPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(d_status)
            title = newspage.check_title()
            self.assertEqual(title, '喜剧片 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load comedy page is ok")
            newspage.quit_browser_()

    def test_sitcome_page(self, s_status=3):
        driver = browser()
        newspage = TvchannelPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(s_status)
            title = newspage.check_title()
            self.assertEqual(title, '连续剧 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load sitcome page is ok")
            newspage.quit_browser_()

    def test_recommandnec_page(self):
        elemen_loc = (By.LINK_TEXT, '西雅图夜未眠')
        driver = browser()
        newspage = TvchannelPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(*elemen_loc)
            newspage.click_(element)
            newspage.switch_new_window_()
            title = newspage.check_title()
            self.assertEqual(title, '西雅图夜未眠 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load recommandnec page is ok")
            newspage.quit_browser_()

    def test_lastnec_page(self):
        elemen_loc = (By.LINK_TEXT, '三国演义06')
        driver = browser()
        newspage = TvchannelPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(*elemen_loc)
            newspage.click_(element)
            title = newspage.check_title()
            self.assertEqual(title, '三国演义06 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load lastnec page is ok")
            newspage.quit_browser_()

    def test_hotnec_page(self):
        elemen_loc = (By.LINK_TEXT, '刀剑笑')
        driver = browser()
        newspage = TvchannelPage(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(*elemen_loc)
            newspage.click_(element)
            title = newspage.check_title()
            self.assertEqual(title, '刀剑笑 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load hotnec page is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

