# -*- coding:UTF-8 -*-
import unittest
from driver import *
from util.myunit import StartEnd
from PageAction import *
from log_print import *


class OpenBrowser(Page):
    '''初始页面需要的方法'''
    url='/'
    def check_title(self):#验证title值
        return self.driver.title


class TestOpenBrowser(StartEnd):
    '''执行测试'''
    def test_open_browser(self):#打开浏览器
        driver=browser()
        logger=get_log('test_open_browser')
        logger.info("Start test_open_browser_")
        try:
            open_browser=OpenBrowser(driver)
            open_browser.open_browser_()
            self.assertEqual(open_browser.check_title(),'帝国网站管理系统 - Powered by EmpireCMS')
        except Exception as msg:
            logger.error(msg)
        finally:
            logger.info("open browser is ok")
            open_browser.quit_browser_()

if __name__ == '__main__':
    unittest.main()


