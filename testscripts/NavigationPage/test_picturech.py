# -*- coding:UTF-8 -*-
import unittest

from testscripts.Login.test_login import Login
from action.driver import *
from util.log_print import *
from util.myunit import StartEnd
from test_data.testdata import testDataInfo


class Picturech(Login):
    url='/'
    def load_master_page(self, type, el_loc):
        el = self.find_element_(type, el_loc)
        self.click_(el)

    def load_part_page(self, type, el_loc, status):
        el = self.find_elements_(type, el_loc)
        self.click_(el[status])
        return el

    def check_title(self):
        return self.title_()

class TestPicturech(StartEnd):
    logger=get_log("test Picturechannel_page")
    data=testDataInfo('Picturech')['Picturech']
    def test_picturech_page(self):
        self.logger.info("Start test picturech_page")
        driver=browser()
        newspage =Picturech(driver)
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
            self.logger.info("test picturech page is end")
            newspage.quit_browser_()

    def test_star_page(self):
        self.logger.info("Start test star_page ")
        driver = browser()
        newspage = Picturech(driver)
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
                self.data['star_page']['star_status'][2]['value']
            )
            title=newspage.check_title()
            self.assertEqual(title,self.data['star_page']['check_star'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test star page is end")
            newspage.quit_browser_()

    def test_nature_page(self):
        driver = browser()
        newspage = Picturech(driver)
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
                self.data['nature_page']['nature_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title, self.data['nature_page']['check_nature'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test nature page is end")
            newspage.quit_browser_()

    def test_animotion_page(self):
        self.logger.info("Start test animotion_page")
        driver = browser()
        newspage = Picturech(driver)
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
                self.data['animotion_page']['animotion_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['animotion_page']['check_animotion'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test animotion page is end")
            newspage.quit_browser_()

    def test_recommand_page(self):
        self.logger.info("Start test recommand_page")
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            element = newspage.find_element_(
                self.data['recommand_page']['ele1'][1]['type'],
                self.data['recommand_page']['ele1'][2]['value']
            )
            newspage.click_(element)
            newspage.switch_new_window_()
            title = newspage.check_title()
            self.assertEqual(title,self.data['recommand_page']['check_re'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test recommandnef page is end")
            newspage.quit_browser_()

    def test_lastfresh_page(self):
        self.logger.info("Start test lastfresh_page")
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            element = newspage.find_element_(
                self.data['lastfresh_page']['ele1'][1]['type'],
                self.data['lastfresh_page']['ele1'][2]['value']
            )
            newspage.click_(element)
            title = newspage.check_title()
            self.assertEqual(title,self.data['lastfresh_page']['check_fresh'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test lastfresh_page is end")
            newspage.quit_browser_()

    def test_hotclick_page(self):
        self.logger.info("Start test hotclick_page")
        driver = browser()
        newspage = Picturech(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            element = newspage.find_element_(
                self.data['hotclick_page']['ele1'][1]['type'],
                self.data['hotclick_page']['ele1'][2]['value']
            )
            newspage.click_(element)
            title = newspage.check_title()
            self.assertEqual(title,self.data['hotclick_page']['check_hot'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test hotclick page is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

