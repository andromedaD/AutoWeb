# -*- coding:UTF-8 -*-

import unittest

from Login.test_login import Login
from driver import *
from log_print import *
from myunit import StartEnd
from testdata import testDataInfo


class Logout(Login):
    url='/'
    logout_data=testDataInfo('Logout')['Logout']
    logout_type=logout_data['logout_el'][1]['type']
    logout_value=logout_data['logout_el'][2]['value']
    checkinfo_type=logout_data['check_info'][1]['type']
    checkinfo_value=logout_data['check_info'][2]['value']

    def logout(self):
        el=self.find_element_(self.logout_type,self.logout_value)
        self.click_(el)

    def check_logout(self):
        el=self.find_element_(self.checkinfo_type,self.checkinfo_value)
        text=self.text_(el)
        return text

class TestLoginOut(StartEnd):
    logger=get_log('test logout')
    data=testDataInfo('Logout')['Logout']
    def test_logout(self):
        self.logger.info("Start test logout")
        driver=browser()
        newspage=Logout(driver)
        newspage.open_browser_()
        newspage.login_page()
        try:
            newspage.logout()
            newspage.accept_()
            text=newspage.check_logout()
            self.assertEqual(text,self.data['assertvalue'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test logout is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

