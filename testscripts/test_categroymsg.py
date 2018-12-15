# -*- coding:UTF-8 -*-
import  unittest
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

    def  test_search(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element=newspage.find_element(By.CSS_SELECTOR,'input[name="keyboard"]')
            newspage.send_keys_(element,"东城区")
            Select(newspage.find_element(By.CSS_SELECTOR,"select[name='classid']")).select_by_value("10")
            element2=newspage.find_element(By.CSS_SELECTOR,'input[name="Submit2"]')
            newspage.click_(element2)
            newspage.switch_new_window_()
            title=newspage.title_()
            self.assertEqual(title,'东城区 搜索结果 - Powered by EmpireCMS')
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test search is ok ")
            newspage.quit_browser_()

    def test_addinfo(self):
        driver=browser()
        newspage=CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element=newspage.find_element(By.LINK_TEXT,'发布信息')
            newspage.click_(element)
            newspage.switch_new_window_()
            Select(newspage.find_element(By.CSS_SELECTOR,'select[name="classid"]')).select_by_value("11")
            element1=newspage.find_element(By.CSS_SELECTOR,'input[type="submit"]')
            newspage.click_(element1)
            newspage.switch_new_window_()
            title=newspage.title_()
            self.assertEqual(title,'增加信息')
            element2=newspage.find_element(By.CSS_SELECTOR,'td:nth-child(2) > input[type="text"]')
            newspage.send_keys_(element2,"东城区雨花小区")
            element3=newspage.find_element(By.CSS_SELECTOR,"tr>td>textarea#smalltext")
            newspage.send_keys_(element3,"租金平均10000")
            element4=newspage.find_element(By.CSS_SELECTOR,'input#email')
            newspage.clear_(element4)
            newspage.send_keys_(element4,"11223@qq.com")
            element5=newspage.find_element(By.CSS_SELECTOR,"input[type='submit']:nth-child(1)")
            newspage.click_(element5)
            element6=newspage.find_element(By.LINK_TEXT,'管理分类信息')
            newspage.click_(element6)
            element7=newspage.find_element(By.LINK_TEXT,'东城区雨花小区')
            self.assertTrue(element7)
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test addinfo is ok")
            newspage.quit_browser_()

    def test_areamap(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element=newspage.find_element(By.LINK_TEXT,'东城区')
            newspage.click_(element)
            newspage.switch_new_window_()
            element1=newspage.find_element(By.CSS_SELECTOR,'table[class="line_bottom"]')
            self.assertTrue(element1)
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test areamap  is ok ")
            newspage.quit_browser_()

    def test_house(self):
        driver=browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element=newspage.find_element(By.LINK_TEXT,'房屋求租')
            newspage.click_(element)
            title=newspage.title_()
            self.assertEqual(title,'房屋求租 - Powered by EmpireCMS')
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test house is ok")
            newspage.quit_browser_()

    def test_pc(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(By.LINK_TEXT, '电脑配件')
            newspage.click_(element)
            title = newspage.title_()
            self.assertEqual(title, '电脑配件 - Powered by EmpireCMS')
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test pc is ok")
            newspage.quit_browser_()

    def test_citylife(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(By.LINK_TEXT, '本地新闻')
            newspage.click_(element)
            title = newspage.title_()
            self.assertEqual(title, '本地新闻 - Powered by EmpireCMS')
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test citylife is ok")
            newspage.quit_browser_()

    def test_job(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(By.LINK_TEXT, '工程技术')
            newspage.click_(element)
            title = newspage.title_()
            self.assertEqual(title, '工程技术 - Powered by EmpireCMS')
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test job is ok")
            newspage.quit_browser_()
    def test_hotclick(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.type_username()
        newspage.load_master_page()
        try:
            element = newspage.find_element(By.LINK_TEXT, '德外/新房/急于出租')
            newspage.click_(element)
            title = newspage.title_()
            self.assertEqual(title, '德外/新房/急于出租 - Powered by EmpireCMS')
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test hotclick is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

