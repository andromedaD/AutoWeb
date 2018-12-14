# -*- coding:UTF-8 -*-
import  unittest
from time import sleep
from selenium.webdriver.common.by import By
from log_print import *
from myunit import StartEnd
from test_login import Login
from driver import *

class CategroyMsg(Login):
    url='/'
    def load_master_page(self):
        element=self.find_element(By.LINK_TEXT,'分类信息')
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

class TestCategroyMsg(StartEnd):
    logger=get_log("test categroy_msg_page")
    def test_categroymsg_page(self):
        driver=browser()
        newspage =CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            title=newspage.check_title()
            self.assertEqual(title,'分类信息 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load category msg page is ok")
            newspage.quit_browser_()

    def test_house_page(self,h_status=0):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(h_status)
            title=newspage.check_title()
            self.assertEqual(title,'房屋信息 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load house page is ok")
            newspage.quit_browser_()

    def test_fleamall_page(self, n_status=1):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '跳蚤市场 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load fleamall page is ok")
            newspage.quit_browser_()

    def test_citylife_page(self, n_status=2):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '同城生活 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load citylife page is ok")
            newspage.quit_browser_()

    def test_job_page(self, n_status=3):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '求职招聘 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load job page is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

