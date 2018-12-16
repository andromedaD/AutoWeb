# -*- coding:UTF-8 -*-
import unittest
from selenium.webdriver.common.by import By
from log_print import *
from testdata import *
from driver import *
from PageAction import *
from myunit import StartEnd

class Register(Page):
    url='/'
    testdata = testDataInfo()['register']
    register_element_loc=(By.NAME,testdata['register_element_loc'])
    nextbutton_element_loc=(By.NAME,testdata['nextbutton_element_loc'])
    corporate_select_loc=(By.XPATH,testdata['corporate_select_loc'])
    username_loc = (By.NAME, testdata['username_loc'])
    password_loc = (By.NAME, testdata['password_loc'])
    repassword_loc = (By.NAME, testdata['repassword_loc'])
    email_loc = (By.NAME, testdata['email_loc'])
    company_loc = (By.NAME, testdata['company_loc'])
    truename_loc = (By.NAME, testdata['truename_loc'])
    mycall_loc = (By.NAME, testdata['mycall_loc'])

    def load_member_center(self):#进入会员中心页面
        register_element=self.find_element(*self.register_element_loc)
        self.click_(register_element)
        sleep(3)
        self.switch_new_window_()#切换到当前页面，会员中心页面
    def load_regular_member(self):#进入会员中心>普通会员页面
        next_button_element=self.find_element(*self.nextbutton_element_loc)
        self.click_(next_button_element)
        sleep(3)
        self.switch_new_window_()
        return 0
    def load_corporate_member(self):#进入会员中心>企业会员页面
        single_select_element=self.find_element(*self.corporate_select_loc)
        self.click_(single_select_element)
        sleep(1)
        next_button_element = self.find_element(*self.nextbutton_element_loc)
        self.click_(next_button_element)
        sleep(3)
        self.switch_new_window_()
        return 1
    def type_user_info(self,username,email,status):#输入相关信息，username和email可能会重复所以放在外面
        type_user_element=self.find_element(*self.username_loc)
        self.clear_(type_user_element)
        self.send_keys_(type_user_element,username)
        sleep(1)
        type_password1_element=self.find_element(*self.password_loc)
        self.clear_(type_password1_element)
        self.send_keys_(type_password1_element, self.testdata['password'])
        sleep(1)
        type_password2_element = self.find_element( *self.repassword_loc)
        self.clear_(type_password2_element)
        self.send_keys_(type_password2_element,self.testdata['repassword'])
        sleep(1)
        type_eamil_element = self.find_element( *self.email_loc)
        self.clear_(type_eamil_element)
        self.send_keys_(type_eamil_element, email)
        sleep(1)
        if status==1:
            type_company_element=self.find_element(*self.company_loc)
            self.clear_(type_company_element)
            self.send_keys_(type_company_element, self.testdata['company'])
            sleep(1)
            type_true_element = self.find_element( *self.truename_loc)
            self.clear_(type_true_element)
            self.send_keys_(type_true_element, self.testdata['truename'])
            sleep(1)
            type_mycall_element = self.find_element( *self.mycall_loc)
            self.clear_(type_mycall_element)
            self.send_keys_(type_mycall_element,self.testdata['mycall'])
            sleep(1)
        else:
            pass
        # type_true_element = self.find_element(By.ID, 'truename')
        # self.clear_(type_true_element)
        # self.send_keys_(type_true_element, '王治本')
        # sleep(1)
        # type_oicq_element = self.find_element(By.ID, 'oicq')
        # self.clear_(type_oicq_element)
        # self.send_keys_(type_oicq_element, '123@qq.com')
        # sleep(1)
        # type_msn_element = self.find_element(By.ID, 'msn')
        # self.clear_(type_msn_element)
        # self.send_keys_(type_msn_element, '123@msn.com')
        # sleep(1)
        #
        # type_mycall_element = self.find_element(By.ID, 'mycall')
        # self.clear_(type_mycall_element)
        # self.send_keys_(type_mycall_element, '1511515151')
        # sleep(1)
        #
        # type_phone_element = self.find_element(By.ID, 'phone')
        # self.clear_(type_phone_element)
        # self.send_keys_(type_phone_element, '32131232321')
        # sleep(1)
        #
        # type_address_element = self.find_element(By.ID, 'address')
        # self.clear_(type_address_element)
        # self.send_keys_(type_address_element, '南京江宁')
        # sleep(1)
        # type_zip_element = self.find_element(By.ID, 'zip')
        # self.clear_(type_zip_element)
        # self.send_keys_(type_zip_element, '212400')
        # sleep(1)
        # type_saytext_element = self.find_element(By.ID, 'saytext')
        # self.clear_(type_saytext_element)
        # self.send_keys_(type_saytext_element, 'hello')
        # sleep(1)
        type_register_element = self.find_element(By.NAME, 'Submit')
        self.click_(type_register_element)
        sleep(4)

class TestRegister(StartEnd):
    '''注册操作方法'''
    testdata = testDataInfo()['register']#测试数据
    def test_regular_register(self):#普通会员注册成功测试用例
        driver=browser()
        logger=get_log("test_regular_member_register")
        logger.info("Start test regular member register")
        register_page = Register(driver)
        register_page.open_browser_()
        register_page.load_member_center()
        sleep(3)
        status=register_page.load_regular_member()
        try:
            register_page.type_user_info(self.testdata['username'][0],self.testdata['email'][0],status)
            register_title=register_page.title_()
            self.assertEqual(register_title,'会员中心')
        except Exception as msg:
            logger.error(msg)
            register_page.quit_browser_()
        finally:
            logger.info("test regular member register is end")
            register_page.quit_browser_()
    def test_corporate_register(self):#企业会员注册成功测试用例
        driver = browser()
        logger = get_log("test_corporate_member_register")
        logger.info("Start test corporate member register")
        register_page = Register(driver)
        register_page.open_browser_()
        register_page.load_member_center()
        sleep(1)
        status =register_page.load_corporate_member()
        try:
            register_page.type_user_info(self.testdata['username'][1],self.testdata['email'][1],status)
            register_title = register_page.title_()
            self.assertEqual(register_title, '会员中心')
        except Exception as msg:
            logger.error(msg)
            register_page.quit_browser_()
        finally:
            logger.info("test corporate member register is end")
            register_page.quit_browser_()

if __name__ == '__main__':
    unittest.main()

