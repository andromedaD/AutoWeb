# -*- coding:UTF-8 -*-
import unittest

from testscripts.Login.test_login import Login
from action.driver import *
from util.log_print import *
from util.myunit import StartEnd
from test_data.testdata import testDataInfo


class NewsPage(Login):
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

class TestNewsPage(StartEnd):
    logger=get_log("test news_page")
    data=testDataInfo('News')['News']
    def test_news_page(self):
        self.logger.info("Start test news_page")
        driver=browser()
        newspage = NewsPage(driver)
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
            self.logger.info("test news page is end")
            newspage.quit_browser_()

    def test_homenews_page(self):
        self.logger.info("Start test homenews_page")
        driver = browser()
        newspage = NewsPage(driver)
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
                self.data['homenews_page']['homenews_status'][2]['value']
            )
            title=newspage.check_title()
            self.assertEqual(title,self.data['homenews_page']['check_homenews'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test home news page is end")
            newspage.quit_browser_()

    def test_nationalnews_page(self):
        self.logger.info("Start test nationalnews_page")
        driver = browser()
        newspage = NewsPage(driver)
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
                self.data['nationalnews_page']['nationalnews_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['nationalnews_page']['check_nationalnews'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test nation news page is end")
            newspage.quit_browser_()

    def test_disportnews_page(self):
        self.logger.info("Start test disportnews_page")
        driver = browser()
        newspage = NewsPage(driver)
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
                self.data['disportnews_page']['disportnews_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['disportnews_page']['check_disportnews'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test disport news page is end")
            newspage.quit_browser_()

    def test_sportnews_page(self):
        self.logger.info("Start test sportnews_page")
        driver = browser()
        newspage = NewsPage(driver)
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
                self.data['sportnews_page']['sportnews_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['sportnews_page']['check_sportnews'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test sport news page is end")
            newspage.quit_browser_()


    def test_recommandnews_page(self):
        self.logger.info("Start test recommandnews_page")
        driver = browser()
        newspage = NewsPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1=newspage.find_element_(
                self.data['recommandnews_page']['ele1'][1]['type'],
                self.data['recommandnews_page']['ele1'][2]['value']
            )
            newspage.click_(ele1)
            newspage.switch_new_window_()
            title = newspage.check_title()
            self.assertEqual(title,self.data['recommandnews_page']['check_re'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test recommandnews page is end")
            newspage.quit_browser_()

    def test_lastfresh_page(self):
        self.logger.info("Start test lastfresh_page")
        driver = browser()
        newspage = NewsPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1 = newspage.find_elements_(
                self.data['lastfresh_page']['ele1'][1]['type'],
                self.data['lastfresh_page']['ele1'][2]['value']
            )[self.data['lastfresh_page']['status'][2]['value']]
            newspage.click_(ele1)
            title = newspage.check_title()
            self.assertEqual(title,self.data['lastfresh_page']['check_fresh'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test lastfresh_page is ok")
            newspage.quit_browser_()

    def test_hotclick_page(self):
        self.logger.info("Start test hotclick_page")
        driver = browser()
        newspage = NewsPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1= newspage.find_elements_(
                self.data['hotclick_page']['ele1'][1]['type'],
                self.data['hotclick_page']['ele1'][2]['value']
            )[self.data['hotclick_page']['status'][2]['value']]
            newspage.click_(ele1)
            title = newspage.check_title()
            self.assertEqual(title,self.data['hotclick_page']['check_hot'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test hotclick_page is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()
