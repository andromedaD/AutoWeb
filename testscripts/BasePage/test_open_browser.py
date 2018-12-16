# -*- coding:UTF-8 -*-
import unittest
from driver import *
from util.myunit import StartEnd
from PageAction import *
from log_print import *
from testdata import testDataInfo

class BasePage(Page):
    '''初始页面需要的方法'''
    url='/'
    def check_title(self):#验证title值
        return self.driver.title


class TestBasePage(StartEnd):
    '''执行测试'''
    logger=get_log('test BasePage')
    data=testDataInfo('Basepage')['Basepage']
    def test_open_browser(self):#打开浏览器
        driver=browser()
        self.logger.info("Start test_open_browser_")
        try:
            newspage=BasePage(driver)
            newspage.open_browser_()
            self.assertEqual(newspage.check_title(),self.data['check_info'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("open browser is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()


