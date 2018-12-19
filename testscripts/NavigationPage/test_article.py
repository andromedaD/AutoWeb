# -*- coding:UTF-8 -*-
import unittest

from testscripts.Login.test_login import Login
from action.driver import *
from util.log_print import *
from util.myunit import StartEnd
from test_data.testdata import testDataInfo

class ArticlePage(Login):
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

class TestArticlePage(StartEnd):
    logger=get_log("test Articl_page")
    data=testDataInfo('Article')['Article']

    def test_article_page(self):
        self.logger.info("Start test article_page ")
        driver=browser()
        newspage =ArticlePage(driver)
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
            self.logger.info("test article page is end")
            newspage.quit_browser_()

    def test_novel_page(self):
        self.logger.info("Start test novel ")
        driver = browser()
        newspage = ArticlePage(driver)
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
                self.data['n_status'][2]['value']
                                    )
            title=newspage.check_title()
            self.assertEqual(title,self.data['check_nv'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test novel page is end")
            newspage.quit_browser_()

    def test_porse_page(self):
        self.logger.info("Start test porse_page")
        driver = browser()
        newspage = ArticlePage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value'])
        try:
            newspage.load_part_page(
                self.data['part_page'][1]['type'],
                self.data['part_page'][2]['value'],
                self.data['p_status'][2]['value']
                                    )
            title = newspage.check_title()
            self.assertEqual(title, self.data['check_pr'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test porse page is end")
            newspage.quit_browser_()

    def test_portry_page(self, n_status=2):
        self.logger.info("Start test portry")
        driver = browser()
        newspage = ArticlePage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value'])
        try:
            newspage.load_part_page(
                self.data['part_page'][1]['type'],
                self.data['part_page'][2]['value'],
                self.data['portry_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['check_portry'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test poetry page is end")
            newspage.quit_browser_()

if __name__ == '__main__':

    unittest.main()
