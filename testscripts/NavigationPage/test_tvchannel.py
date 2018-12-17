# -*- coding:UTF-8 -*-
import unittest

from Login.test_login import Login
from driver import *
from log_print import *
from myunit import StartEnd
from testdata import testDataInfo

class TvchannelPage(Login):
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

class TestTvchannelPage(StartEnd):
    logger=get_log("test tvchannel_page")
    data=testDataInfo('TVchannel')['TVchannel']

    def test_tvchannel_page(self):
        self.logger.info("Start test tvchannel")
        driver=browser()
        newspage =TvchannelPage(driver)
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
            self.logger.info("test tvchannel page is end")
            newspage.quit_browser_()

    def test_actionvideo_page(self):
        self.logger.info("Start test actionvideo_page")
        driver = browser()
        newspage = TvchannelPage(driver)
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
                self.data['actionvideo_page']['actionvideo_status'][2]['value']
            )
            title=newspage.check_title()
            self.assertEqual(title,self.data['actionvideo_page']['check_actionvideo'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test action video page is end")
            newspage.quit_browser_()

    def test_lovevideo_page(self):
        self.logger.info("Start test lovevideo_page")
        driver = browser()
        newspage = TvchannelPage(driver)
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
                self.data['lovevideo_page']['lovevideo_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['lovevideo_page']['check_lovevideo'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test lovevideo page is end")
            newspage.quit_browser_()

    def test_comedy_page(self):
        self.logger.info("Start test comedy_page")
        driver = browser()
        newspage = TvchannelPage(driver)
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
                self.data['comedy_page']['comedy_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['comedy_page']['check_comedy'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test comedy page is end")
            newspage.quit_browser_()

    def test_sitcome_page(self):
        self.logger.info("Start test sitcome_page")
        driver = browser()
        newspage = TvchannelPage(driver)
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
                self.data['sitcome_page']['sitcome_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['sitcome_page']['check_book'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test sitcome page is end")
            newspage.quit_browser_()

    def test_recommand_page(self):
        self.logger.info("Start test recommand_page")
        driver = browser()
        newspage = TvchannelPage(driver)
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
            self.logger.info("tesst recommandnec page is end")
            newspage.quit_browser_()

    def test_lastfresh_page(self):
        self.logger.info("Start test lastfresh_page")
        driver = browser()
        newspage = TvchannelPage(driver)
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
            self.logger.info("test lastfresh_page is end")
            newspage.quit_browser_()

    def test_hotclick_page(self):
        self.logger.info("Start test hotclick_page")
        driver = browser()
        newspage = TvchannelPage(driver)
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
            self.logger.info("load hotnec page is ok")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

