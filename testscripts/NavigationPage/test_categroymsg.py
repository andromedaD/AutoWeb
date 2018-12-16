# -*- coding:UTF-8 -*-
import unittest
from selenium.webdriver.support.select import Select
from Login.test_login import Login
from driver import *
from log_print import *
from myunit import StartEnd
from testdata import testDataInfo

class CategroyMsg(Login):
    url='/'

    def load_master_page(self,type,el_loc):
        el=self.find_element_(type,el_loc)
        self.click_(el)

    def load_part_page(self,type,el_loc,status):
        el=self.find_elements_(type,el_loc)
        self.click_(el[status])
        return el

    def check_title(self):
        return self.title_()

class TestCategroyMsg(StartEnd):
    logger=get_log("test categroy_msg_page")
    data=testDataInfo('Categroymsg')['Categroymsg']
    # def test_categroymsg_page(self):
    #     self.logger.info("Start test categroymsg_page")
    #     driver=browser()
    #     newspage =CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.login_page()
    #     newspage.load_master_page(self.data['master_page'][1]['type'],
    #                               self.data['master_page'][2]['value']
    #                               )
    #     try:
    #         title=newspage.check_title()
    #         self.assertEqual(title,self.data['check_ma'][2]['value'])
    #     except Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test category msg page is end")
    #         newspage.quit_browser_()
    #
    # def test_house_page(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.login_page()
    #     newspage.load_master_page(self.data['master_page'][1]['type'],
    #                               self.data['master_page'][2]['value']
    #                               )
    #     try:
    #         newspage.load_part_page(self.data['part_page'][1]['type'],
    #                                 self.data['part_page'][2]['value'],
    #                                 self.data['h_status'][2]['value']
    #                                 )
    #         title=newspage.check_title()
    #         self.assertEqual(title,self.data['check_h'][2]['value'])
    #     except Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test house page is end")
    #         newspage.quit_browser_()
    #
    # def test_fleamall_page(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.login_page()
    #     newspage.load_master_page(self.data['master_page'][1]['type'],
    #                               self.data['master_page'][2]['value']
    #                               )
    #     try:
    #         newspage.load_part_page(self.data['part_page'][1]['type'],
    #                                 self.data['part_page'][2]['value'],
    #                                 self.data['fl_status'][2]['value']
    #                                 )
    #         title = newspage.check_title()
    #         self.assertEqual(title,self.data['check_fl'][2]['value'])
    #     except Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test fleamall page is end")
    #         newspage.quit_browser_()
    #
    # def test_citylife_page(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.login_page()
    #     newspage.load_master_page(self.data['master_page'][1]['type'],
    #                               self.data['master_page'][2]['value']
    #                               )
    #     try:
    #         newspage.load_part_page(self.data['part_page'][1]['type'],
    #                                 self.data['part_page'][2]['value'],
    #                                 self.data['city_status'][2]['value']
    #                                 )
    #         title = newspage.check_title()
    #         self.assertEqual(title,self.data['check_city'][2]['value'])
    #     except Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test citylife page is end")
    #         newspage.quit_browser_()
    #
    # def test_job_page(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.login_page()
    #     newspage.load_master_page(self.data['master_page'][1]['type'],
    #                               self.data['master_page'][2]['value']
    #                               )
    #     try:
    #         newspage.load_part_page(self.data['part_page'][1]['type'],
    #                                 self.data['part_page'][2]['value'],
    #                                 self.data['job_status'][2]['value'])
    #         title = newspage.check_title()
    #         self.assertEqual(title,self.data['check_job'][2]['value'])
    #     except Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test job page is end")
    #         newspage.quit_browser_()

    def  test_search(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(self.data['master_page'][1]['type'],
                                  self.data['master_page'][2]['value']
                                  )
        try:
            ele1=newspage.find_element_(self.data['search'][1]['type'],
                                       self.data['search'][2]['value']
                                       )
            newspage.send_keys_(ele1,self.data['search_keys'][2]['value'])
            Select(
                newspage.find_element_(self.data['selector'][1]['type'],
                                          self.data['selector'][2]['value']
                                          )).select_by_value(str(self.data['selector_value'][2]['value']))
            ele2=newspage.find_element_(self.data['search_button'][1]['type'],
                                          self.data['search_button'][2]['value']
                                        )
            newspage.click_(ele2)
            newspage.switch_new_window_()
            title=newspage.title_()
            self.assertEqual(title,self.data['check_search'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test search is end ")
            newspage.quit_browser_()

    # def test_addinfo(self):
    #     driver=browser()
    #     newspage=CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.login_page()
    #     newspage.load_master_page(self.data['master_page'][1]['type'],
    #                               self.data['master_page'][2]['value']
    #                               )
    #     try:
    #         element=newspage.find_element(By.LINK_TEXT,'发布信息')
    #         newspage.click_(element)
    #         newspage.switch_new_window_()
    #         Select(newspage.find_element(By.CSS_SELECTOR,'select[name="classid"]')).select_by_value("11")
    #         element1=newspage.find_element(By.CSS_SELECTOR,'input[type="submit"]')
    #         newspage.click_(element1)
    #         newspage.switch_new_window_()
    #         title=newspage.title_()
    #         self.assertEqual(title,'增加信息')
    #         element2=newspage.find_element(By.CSS_SELECTOR,'td:nth-child(2) > input[type="text"]')
    #         newspage.send_keys_(element2,"东城区雨花小区")
    #         element3=newspage.find_element(By.CSS_SELECTOR,"tr>td>textarea#smalltext")
    #         newspage.send_keys_(element3,"租金平均10000")
    #         element4=newspage.find_element(By.CSS_SELECTOR,'input#email')
    #         newspage.clear_(element4)
    #         newspage.send_keys_(element4,"11223@qq.com")
    #         element5=newspage.find_element(By.CSS_SELECTOR,"input[type='submit']:nth-child(1)")
    #         newspage.click_(element5)
    #         element6=newspage.find_element(By.LINK_TEXT,'管理分类信息')
    #         newspage.click_(element6)
    #         element7=newspage.find_element(By.LINK_TEXT,'东城区雨花小区')
    #         self.assertTrue(element7)
    #     except Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test addinfo is ok")
    #         newspage.quit_browser_()
    #
    # def test_areamap(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.type_username()
    #     newspage.load_master_page()
    #     try:
    #         element=newspage.find_element(By.LINK_TEXT,'东城区')
    #         newspage.click_(element)
    #         newspage.switch_new_window_()
    #         element1=newspage.find_element(By.CSS_SELECTOR,'table[class="line_bottom"]')
    #         self.assertTrue(element1)
    #     except Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test areamap  is ok ")
    #         newspage.quit_browser_()
    #
    # def test_house(self):
    #     driver=browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.type_username()
    #     newspage.load_master_page()
    #     try:
    #         element=newspage.find_element(By.LINK_TEXT,'房屋求租')
    #         newspage.click_(element)
    #         title=newspage.title_()
    #         self.assertEqual(title,'房屋求租 - Powered by EmpireCMS')
    #     except  Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test house is ok")
    #         newspage.quit_browser_()
    #
    # def test_pc(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.type_username()
    #     newspage.load_master_page()
    #     try:
    #         element = newspage.find_element(By.LINK_TEXT, '电脑配件')
    #         newspage.click_(element)
    #         title = newspage.title_()
    #         self.assertEqual(title, '电脑配件 - Powered by EmpireCMS')
    #     except  Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test pc is ok")
    #         newspage.quit_browser_()
    #
    # def test_citylife(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.type_username()
    #     newspage.load_master_page()
    #     try:
    #         element = newspage.find_element(By.LINK_TEXT, '本地新闻')
    #         newspage.click_(element)
    #         title = newspage.title_()
    #         self.assertEqual(title, '本地新闻 - Powered by EmpireCMS')
    #     except  Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test citylife is ok")
    #         newspage.quit_browser_()
    #
    # def test_job(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.type_username()
    #     newspage.load_master_page()
    #     try:
    #         element = newspage.find_element(By.LINK_TEXT, '工程技术')
    #         newspage.click_(element)
    #         title = newspage.title_()
    #         self.assertEqual(title, '工程技术 - Powered by EmpireCMS')
    #     except  Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test job is ok")
    #         newspage.quit_browser_()
    # def test_hotclick(self):
    #     driver = browser()
    #     newspage = CategroyMsg(driver)
    #     newspage.open_browser_()
    #     newspage.type_username()
    #     newspage.load_master_page()
    #     try:
    #         element = newspage.find_element(By.LINK_TEXT, '德外/新房/急于出租')
    #         newspage.click_(element)
    #         title = newspage.title_()
    #         self.assertEqual(title, '德外/新房/急于出租 - Powered by EmpireCMS')
    #     except  Exception as msg:
    #         self.logger.error(msg)
    #         newspage.quit_browser_()
    #     finally:
    #         self.logger.info("test hotclick is ok")
    #         newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

