# -*- coding:UTF-8 -*-
import unittest

from testscripts.Login.test_login import Login
from action.driver import *
from util.log_print import *
from util.myunit import StartEnd
from test_data.testdata import testDataInfo


class ShopPage(Login):
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

class TestShopPage(StartEnd):
    logger=get_log("test shop_page")
    data=testDataInfo('Shop')['Shop']
    def test_shop_page(self):
        self.logger.info("Start test shop_page")
        driver=browser()
        newspage =ShopPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            title=newspage.check_title()
            self.assertEqual(title,self.data['check_ma'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test shop page is end")
            newspage.quit_browser_()

    def test_digit_page(self):
        self.logger.info("Start test digit_page")
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            newspage.load_part_page(
                self.data['part_page'][1]['type'],
                self.data['part_page'][2]['value'],
                self.data['digit_page']['digit_status'][2]['value']
            )
            title=newspage.check_title()
            self.assertEqual(title,self.data['digit_page']['check_digit'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test digit page is end")
            newspage.quit_browser_()

    def test_dianqi_page(self):
        self.logger.info("Start test dianqi_page")
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            newspage.load_part_page(
                self.data['part_page'][1]['type'],
                self.data['part_page'][2]['value'],
                self.data['dianqi_page']['dianqi_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['dianqi_page']['check_dianqi'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test dianqi page is end")
            newspage.quit_browser_()

    def test_pc_page(self):
        self.logger.info("Start test pc_page")
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            newspage.load_part_page(
                self.data['part_page'][1]['type'],
                self.data['part_page'][2]['value'],
                self.data['pc_page']['pc_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['pc_page']['check_pc'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test pc page is end")
            newspage.quit_browser_()

    def test_book_page(self):
        self.logger.info("Start test book_page")
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            newspage.load_part_page(
                self.data['part_page'][1]['type'],
                self.data['part_page'][2]['value'],
                self.data['book_page']['book_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['book_page']['check_book'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test book page is end")
            newspage.quit_browser_()

    def test_recommand_page(self):
        self.logger.info("Start test recommand_page")
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1 = newspage.find_element_(
                self.data['recommand_page']['ele1'][1]['type'],
                self.data['recommand_page']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            newspage.switch_new_window_()
            title = newspage.check_title()
            self.assertEqual(title,self.data['recommand_page']['check_recommand'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test recommandned page is end")
            newspage.quit_browser_()

    def test_lastfresh_page(self):
        self.logger.info("Start test lastfresh_page")
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1 = newspage.find_element_(
                self.data['lastfresh_page']['ele1'][1]['type'],
                self.data['lastfresh_page']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            title = newspage.check_title()
            self.assertEqual(title,self.data['lastfresh_page']['check_lastfresh'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test lastned page is end")
            newspage.quit_browser_()

    def test_hotclick_page(self):
        self.logger.info("Start test hotclick_page")
        driver = browser()
        newspage = ShopPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
            )
        try:
            ele1 = newspage.find_element_(
                self.data['hotclick_page']['ele1'][1]['type'],
                self.data['hotclick_page']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            title = newspage.check_title()
            self.assertEqual(title,self.data['hotclick_page']['check_hotclick'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test hotned page is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

