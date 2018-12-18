# -*- coding:UTF-8 -*-
from action.PageAction import *
from action.driver import *
from util.log_print import *
from util.myunit import *
from test_data.testdata import *


class Login(Page):
    '''登录操作方法'''
    url='/'
    login_data=testDataInfo('Login')['Login']
    uloc_type=login_data['user_el'][1]['type']#username定位方式
    uloc_value=login_data['user_el'][2]['value']#username定位值
    ploc_type=login_data['pwd_el'][1]['type']#password定位方式
    ploc_value=login_data['pwd_el'][2]['value']#password定位值
    sloc_type=login_data['submit_el'][1]['type']#登录按钮定位方式
    sloc_value=login_data['submit_el'][2]['value']#登录按钮定位值
    check_info_type=login_data['check_info'][1]['type']#验证值定位方式
    check_info_value=login_data['check_info'][2]['value']#验证值定位值
    username=login_data['user'][2]['value']#用户名
    password=login_data['password'][2]['value']#登录密码

    def login_page(self):#输入用户名及密码
        user_el=self.find_element_(self.uloc_type,self.uloc_value)
        self.clear_(user_el)
        self.send_keys_(user_el,self.username)
        pwd_el=self.find_element_(self.ploc_type,self.ploc_value)
        self.clear_(pwd_el)
        self.send_keys_(pwd_el,self.password)
        sub_el=self.find_element_(self.sloc_type,self.sloc_value)
        self.click_(sub_el)
        sleep(3)

    def checkinfo(self):#返回验证信息
        check_el=self.find_element_(self.check_info_type,self.check_info_value)
        text=self.text_(check_el)
        return text

class Testlogin(StartEnd):
    '''具体用例执行'''
    logger = get_log('test_login')
    def test_login(self):#登录用例
        driver=browser()
        self.logger.info(u"Start login")
        newspage=Login(driver)
        newspage.open_browser_()
        newspage.login_page()
        try:
            text=newspage.checkinfo()
            self.assertTrue(text)
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info(u"login is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

