# -*- coding:UTF-8 -*-
import unittest

from selenium.webdriver.support.select import Select
from testscripts.Login.test_login import Login
from action.driver import *
from util.log_print import *
from util.myunit import StartEnd
from test_data.testdata import testDataInfo


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
    def test_categroymsg_page(self):
        self.logger.info("Start test categroymsg_page")
        driver=browser()
        newspage =CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(self.data['master_page'][1]['type'],
                                  self.data['master_page'][2]['value']
                                  )
        try:
            title=newspage.check_title()
            self.assertEqual(title,self.data['check_ma'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test category msg page is end")
            newspage.quit_browser_()

    def test_house_page(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(self.data['master_page'][1]['type'],
                                  self.data['master_page'][2]['value']
                                  )
        try:
            newspage.load_part_page(self.data['part_page'][1]['type'],
                                    self.data['part_page'][2]['value'],
                                    self.data['h_status'][2]['value']
                                    )
            title=newspage.check_title()
            self.assertEqual(title,self.data['check_h'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test house page is end")
            newspage.quit_browser_()

    def test_fleamall_page(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(self.data['master_page'][1]['type'],
                                  self.data['master_page'][2]['value']
                                  )
        try:
            newspage.load_part_page(self.data['part_page'][1]['type'],
                                    self.data['part_page'][2]['value'],
                                    self.data['fl_status'][2]['value']
                                    )
            title = newspage.check_title()
            self.assertEqual(title,self.data['check_fl'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test fleamall page is end")
            newspage.quit_browser_()

    def test_citylife_page(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(self.data['master_page'][1]['type'],
                                  self.data['master_page'][2]['value']
                                  )
        try:
            newspage.load_part_page(self.data['part_page'][1]['type'],
                                    self.data['part_page'][2]['value'],
                                    self.data['city_status'][2]['value']
                                    )
            title = newspage.check_title()
            self.assertEqual(title,self.data['check_city'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test citylife page is end")
            newspage.quit_browser_()

    def test_job_page(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(self.data['master_page'][1]['type'],
                                  self.data['master_page'][2]['value']
                                  )
        try:
            newspage.load_part_page(self.data['part_page'][1]['type'],
                                    self.data['part_page'][2]['value'],
                                    self.data['job_status'][2]['value'])
            title = newspage.check_title()
            self.assertEqual(title,self.data['check_job'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test job page is end")
            newspage.quit_browser_()

    def  test_search(self):
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
                                  )
        try:
            ele1=newspage.find_element_(
                self.data['search'][1]['type'],
                self.data['search'][2]['value']
                                       )
            newspage.send_keys_(ele1,self.data['search_keys'][2]['value'])
            Select(
                newspage.find_element_(
                    self.data['selector'][1]['type'],
                    self.data['selector'][2]['value']
                                          )
                ).select_by_value(str(self.data['selector_value'][2]['value']))
            ele2=newspage.find_element_(
                self.data['search_button'][1]['type'],
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

    def test_addinfo(self):
        self.logger.info("Start test addinfo")
        driver=browser()
        newspage=CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
                                  )
        try:
            ele1=newspage.find_element_(
                self.data['addinfo']['ele1'][1]['type'],
                self.data['addinfo']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            newspage.switch_new_window_()
            Select(
                newspage.find_element_(
                self.data['addinfo']['ele2'][1]['type'],
                self.data['addinfo']['ele2'][2]['value'])
            ).select_by_value(
                str(self.data['addinfo']['ele2_value'][2]['value'])
            )
            ele3=newspage.find_element_(
                self.data['addinfo']['ele3'][1]['type'],
                self.data['addinfo']['ele3'][2]['value']
                                        )
            newspage.click_(ele3)
            newspage.switch_new_window_()
            title=newspage.title_()
            self.assertEqual(title,self.data['addinfo']['checkinfo1'][2]['value'])
            ele4=newspage.find_element_(
                self.data['addinfo']['ele4'][1]['type'],
                self.data['addinfo']['ele4'][2]['value']
                                        )
            newspage.send_keys_(ele4,self.data['addinfo']['content1'][2]['value'])
            ele5=newspage.find_element_(
                self.data['addinfo']['ele5'][1]['type'],
                self.data['addinfo']['ele5'][2]['value']
            )
            newspage.send_keys_(ele5,self.data['addinfo']['content2'][2]['value'])
            ele6=newspage.find_element_(
                self.data['addinfo']['ele6'][1]['type'],
                self.data['addinfo']['ele6'][2]['value']
                                        )
            newspage.clear_(ele6)
            newspage.send_keys_(ele6,self.data['addinfo']['content3'][2]['value'])
            ele7=newspage.find_element_(
                self.data['addinfo']['ele7'][1]['type'],
                self.data['addinfo']['ele7'][2]['value']
            )
            newspage.click_(ele7)
            elem8=newspage.find_element_(
                self.data['addinfo']['ele8'][1]['type'],
                self.data['addinfo']['ele8'][2]['value']
            )
            newspage.click_(elem8)
            ele9=newspage.find_element_(
                self.data['addinfo']['ele9'][1]['type'],
                self.data['addinfo']['ele9'][2]['value']
            )
            self.assertTrue(ele9)
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test addinfo is end")
            newspage.quit_browser_()

    def test_areamap(self):
        self.logger.info("Start test areamap")
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1=newspage.find_element_(
                self.data['areamap']['ele1'][1]['type'],
                self.data['areamap']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            newspage.switch_new_window_()
            ele2=newspage.find_element_(
                self.data['areamap']['ele2'][1]['type'],
                self.data['areamap']['ele2'][2]['value']
            )
            self.assertTrue(ele2)
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test areamap  is end ")
            newspage.quit_browser_()

    def test_house(self):
        driver=browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1=newspage.find_element_(
                self.data['house']['ele1'][1]['type'],
                self.data['house']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            title=newspage.title_()
            self.assertEqual(title,self.data['house']['check_info'][2]['value'])
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test house is end")
            newspage.quit_browser_()

    def test_pc(self):
        self.logger.info("Start test pc")
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1= newspage.find_element_(
                self.data['pc']['ele1'][1]['type'],
                self.data['pc']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            title = newspage.title_()
            self.assertEqual(title,self.data['pc']['check_info'][2]['value'])
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test pc is end")
            newspage.quit_browser_()

    def test_citylife(self):
        self.logger.info("Start test citylife")
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1 = newspage.find_element_(
                self.data['citylife']['ele1'][1]['type'],
                self.data['citylife']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            title = newspage.title_()
            self.assertEqual(title, self.data['citylife']['check_info'][2]['value'])
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test citylife is end")
            newspage.quit_browser_()

    def test_job(self):
        self.logger.info("Start test job")
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1 = newspage.find_element_(
                self.data['job']['ele1'][1]['type'],
                self.data['job']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            title = newspage.title_()
            self.assertEqual(title,self.data['job']['check_info'][2]['value'])
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test job is end")
            newspage.quit_browser_()
    def test_hotclick(self):
        self.logger.info("Start test hotclick")
        driver = browser()
        newspage = CategroyMsg(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1 = newspage.find_element_(
            self.data['hotclick']['ele1'][1]['type'],
            self.data['hotclick']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            title = newspage.title_()
            self.assertEqual(title,self.data['hotclick']['check_info'][2]['value'])
        except  Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test hotclick is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

