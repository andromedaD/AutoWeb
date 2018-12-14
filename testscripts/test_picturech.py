# -*- coding:UTF-8 -*-
import  unittest
from time import sleep
from selenium.webdriver.common.by import By
from log_print import *
from myunit import StartEnd
from test_login import Login
from driver import *

class Picturech(Login):
    url='/'
    def load_master_page(self):
        element=self.find_element(By.LINK_TEXT,'图片频道')
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

class TestPicturech(StartEnd):
    logger=get_log("test Picturechannel_page")
    def test_picturech_page(self):
        driver=browser()
        newspage =Picturech(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            title=newspage.check_title()
            self.assertEqual(title,'图片频道 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load picturech page is ok")
            newspage.quit_browser_()

    def test_star_page(self,h_status=0):
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(h_status)
            title=newspage.check_title()
            self.assertEqual(title,'明星风采 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load star page is ok")
            newspage.quit_browser_()

    def test_nature_page(self, n_status=1):
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '自然风景 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load nature page is ok")
            newspage.quit_browser_()

    def test_animotion_page(self, n_status=2):
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            newspage.load_part_page(n_status)
            title = newspage.check_title()
            self.assertEqual(title, '动漫图片 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load animotion page is ok")
            newspage.quit_browser_()

    def test_recommandnef_page(self):
        elemen_loc = (By.CSS_SELECTOR,'img[alt="宋慧乔[图集]"]')
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(*elemen_loc)
            newspage.click_(element)
            newspage.switch_new_window_()
            title = newspage.check_title()
            self.assertEqual(title, '宋慧乔[图集] - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load recommandnef page is ok")
            newspage.quit_browser_()

    def test_lastnef_page(self):
        elemen_loc = (By.CSS_SELECTOR, 'table.box>tbody>tr>td>ul>li>a[title="宋慧乔[图集]"]')
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(*elemen_loc)
            newspage.click_(element)
            title = newspage.check_title()
            self.assertEqual(title, '宋慧乔[图集] - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load lastnef page is ok")
            newspage.quit_browser_()

    def test_hotnef_page(self):
        elemen_loc = (By.CSS_SELECTOR, 'table.box>tbody>tr>td>ol.rank>li.no2>a')
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(*elemen_loc)
            newspage.click_(element)
            title = newspage.check_title()
            self.assertEqual(title, '宋慧乔[图集] - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("load hotnef page is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

