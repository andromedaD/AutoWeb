# -*- coding:UTF-8 -*-
import unittest

from Login.test_login import Login
from driver import *
from log_print import *
from myunit import StartEnd
from testdata import testDataInfo

class DownloadPage(Login):
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

class TestDownloadPage(StartEnd):
    logger=get_log("test download_page")
    data=testDataInfo('Download')['Download']
    def test_download_page(self):
        self.logger.info("Start test downloadpage")
        driver=browser()
        newspage =DownloadPage(driver)
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
            self.logger.info("test download page is end")
            newspage.quit_browser_()

    def test_sys_page(self):
        self.logger.info("Start test sys_page")
        driver = browser()
        newspage = DownloadPage(driver)
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
                self.data['sye_page']['sys_status'][2]['value']
            )
            title=newspage.check_title()
            self.assertEqual(title,self.data['sye_page']['check_sys'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test sys news page is end")
            newspage.quit_browser_()

    def test_nettools_page(self):
        self.logger.info("Start test nettols")
        driver = browser()
        newspage = DownloadPage(driver)
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
                self.data['nettools_page']['net_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['nettools_page']['check_net'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test nettools page is end")
            newspage.quit_browser_()

    def test_safetools_page(self):
        self.logger.info("Start test safetools_page")
        driver = browser()
        newspage = DownloadPage(driver)
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
                self.data['safetools_page']['net_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['safetools_page']['check_safe'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test safetools news page is end")
            newspage.quit_browser_()

    def test_mediatools_page(self):
        self.logger.info("Start test mediatools_page")
        driver = browser()
        newspage = DownloadPage(driver)
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
                self.data['mediatools_page']['media_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['mediatools_page']['check_media'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test sport mediatools page is end")
            newspage.quit_browser_()

    def test_recommand_page(self):
        self.logger.info("Start test recommand_page")
        driver = browser()
        newspage = DownloadPage(driver)
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
            self.assertEqual(title,self.data['recommand_page']['check_re'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test recommandnewb page is end")
            newspage.quit_browser_()

    def test_lastfresh_page(self):
        self.logger.info("Start test lastfresh_page")
        driver = browser()
        newspage = DownloadPage(driver)
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
            self.assertEqual(title,self.data['lastfresh_page']['check_fresh'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test lastfresh page is end")
            newspage.quit_browser_()

    def test_hotclick_page(self):
        self.logger.info("Start test hotclick_page")
        driver = browser()
        newspage = DownloadPage(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1= newspage.find_element_(
                self.data['hotclick_page']['ele1'][1]['type'],
                self.data['hotclick_page']['ele1'][2]['value']
            )
            newspage.click_(ele1)
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

