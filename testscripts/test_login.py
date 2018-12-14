# -*- coding:UTF-8 -*-
from selenium.webdriver.common.by import By
from testdata import *
from driver import *
from PageAction import *
from log_print import *
from myunit import *

class Login(Page):
    '''登录操作方法'''
    testdata=testDataInfo()
    url='/'
    username_element_loc=(By.NAME,testdata['username_element_loc'])
    password_element_loc=(By.NAME,testdata['password_element_loc'])
    submit_element_loc=(By.NAME,testdata['submit_element_loc'])
    check_assert_loc = (By.LINK_TEXT,testdata['check_assert_loc'])

    def type_username(self,username='wangjin',password='123456'):#输入用户名及密码
        user_element=self.find_element(*self.username_element_loc)
        self.clear_(user_element)
        self.send_keys_(user_element,username)
        pasword_element=self.find_element(*self.password_element_loc)
        self.clear_(pasword_element)
        self.send_keys_(pasword_element, password)
        submit_element=self.find_element(*self.submit_element_loc)
        self.click_(submit_element)
        sleep(3)
        # check_assert_element = self.find_element(*self.check_assert_loc)
        # print(self.text_(check_assert_element))
    def check_assert(self):#返回验证信息
        check_assert_element=self.find_element(*self.check_assert_loc)
        check_assert_text_=self.text_(check_assert_element)
        return check_assert_text_

class Testlogin(StartEnd):
    '''具体用例执行'''
    def test_login(self):#登录用例
        driver=browser()
        logger = get_log('test_login')
        logger.info("Start login")
        login_page=Login(driver)
        login_page.open_browser_()
        username = testDataInfo()['username']
        password = testDataInfo()['password']
        login_page.type_username(username, password)
        try:
            checkassert=login_page.check_assert()
            # print(checkassert)
            self.assertEqual(checkassert,testDataInfo()['asset_value'])
        except Exception as msg:
            logger.error(msg)
            login_page.quit_browser_()
        finally:
            logger.info("login is ok")
            login_page.quit_browser_()

if __name__ == '__main__':
    unittest.main()

