# -*- coding:UTF-8 -*-
import unittest
from Login.test_login import Login
from driver import *
from log_print import *
from myunit import StartEnd
from testdata import testDataInfo

class Flashch(Login):
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

class TestFlashch(StartEnd):
    logger=get_log("test Flashchannel_page")
    data=testDataInfo('Flashchannel')['Flashchannel']
    def test_flash_page(self):
        driver=browser()
        newspage =Flashch(driver)
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
            self.logger.info("test flash page is end")
            newspage.quit_browser_()

    def test_game_page(self):
        self.logger.info("Start test game_page")
        driver = browser()
        newspage = Flashch(driver)
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
                self.data['game_page']['game_status'][2]['value']
            )
            title=newspage.check_title()
            self.assertEqual(title,self.data['game_page']['check_game'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test game page is end")
            newspage.quit_browser_()

    def test_music_page(self):
        self.logger.info("Start test music_page")
        driver = browser()
        newspage = Flashch(driver)
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
                self.data['music_page']['music_status'][2]['value']
            )
            title = newspage.check_title()
            self.assertEqual(title,self.data['music_page']['check_music'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test music page is end")
            newspage.quit_browser_()

    def test_recommand_page(self):
        self.logger.info("Start test recommand_page")
        driver = browser()
        newspage = Flashch(driver)
        newspage.open_browser_()
        newspage.login_page()
        newspage.load_master_page(
            self.data['master_page'][1]['type'],
            self.data['master_page'][2]['value']
        )
        try:
            ele1= newspage.find_element_(
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
            self.logger.info("test recommandnee page is end")
            newspage.quit_browser_()

    def test_lastfresh_page(self):
        driver = browser()
        newspage = Flashch(driver)
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
            self.logger.info("test lastfresh_page is end")
            newspage.quit_browser_()

    def test_hotclick_page(self):
        self.logger.info("Start test hotclick")
        driver = browser()
        newspage = Flashch(driver)
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
            self.logger.info("test hotnee page is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

