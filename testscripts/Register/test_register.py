# -*- coding:UTF-8 -*-
import unittest

from action.PageAction import *
from action.driver import *
from util.log_print import *
from util.myunit import StartEnd
from util.random_user_email import *
from test_data.testdata import testDataInfo,testdataWrite

class Register(Page):
    url='/'
    data=testDataInfo('Register')['Register']
    #定义进入注册会员页面方法
    def load_member_center(self):#进入会员中心页面
        try:
            el=self.find_element_(
                self.data['member_center'][1]['type'],
                self.data['member_center'][2]['value']
            )
            self.click_(el)
        except:
            raise TypeError("input is invalid")
        self.switch_new_window_()#切换到当前页面，会员中心页面
    #定义进入注册普通会员页面方法
    def load_regular_member(self):#进入会员中心>普通会员页面
        try:
            el=self.find_element_(
                self.data['regular_member']['next_step'][1]['type'],
                self.data['regular_member']['next_step'][2]['value']
            )
            self.click_(el)
        except:
            raise TypeError("input is  invalid")
        self.switch_new_window_()
    #进入注册企业会员页面方法
    def load_corporate_member(self):#进入会员中心>企业会员页面
        try:
            ele1=self.find_element_(
                self.data['corporate_member']['ele1'][1]['type'],
                self.data['corporate_member']['ele1'][2]['value']
                )
            self.click_(ele1)
            ele2= self.find_element_(
                self.data['corporate_member']['next_step'][1]['type'],
                self.data['corporate_member']['next_step'][2]['value']
            )
            self.click_(ele2)
        except:
            raise TypeError("input is invalid")
        self.switch_new_window_()


class TestRegister(StartEnd):
    '''注册操作方法'''
    logger=get_log("test register")
    data = testDataInfo('Register')['Register']
    #进入注册页
    def test_member_center(self):#会员中心注册成功测试用例
        self.logger.info("Start test member_center")
        driver=browser()
        newspage=Register(driver)
        newspage.open_browser_()
        try:
            newspage.load_member_center()
            title=newspage.title_()
            self.assertEqual(title,self.data['check_member'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test member_center is end")
            newspage.quit_browser_()
    #普通会员注册
    def test_regular_register(self):#普通会员注册成功测试用例
        self.logger.info("Start test regular member register")
        driver=browser()
        newspage = Register(driver)
        newspage.open_browser_()
        newspage.load_member_center()
        newspage.load_regular_member()
        try:
            ele1=newspage.find_element_(
                self.data['regular_member']['username_loc'][1]['type'],
                self.data['regular_member']['username_loc'][2]['value']
            )
            newspage.send_keys_(ele1,get_userNameAndPassword())

            ele2=newspage.find_element_(
                self.data['regular_member']['password_loc'][1]['type'],
                self.data['regular_member']['password_loc'][2]['value']
            )
            newspage.send_keys_(ele2,'123456')

            ele3=newspage.find_element_(
                self.data['regular_member']['repassword_loc'][1]['type'],
                self.data['regular_member']['repassword_loc'][2]['value']
            )
            newspage.send_keys_(ele3,'123456')

            ele4=newspage.find_element_(
                self.data['regular_member']['email_loc'][1]['type'],
                self.data['regular_member']['email_loc'][2]['value']
            )
            newspage.send_keys_(ele4,get_Email())

            ele5=newspage.find_element_(
                self.data['regular_member']['truename_loc'][1]['type'],
                self.data['regular_member']['truename_loc'][2]['value']
                        )
            newspage.send_keys_(ele5,'大王')
            ele6=newspage.find_element_(
                self.data['regular_member']['qq_loc'][1]['type'],
                self.data['regular_member']['qq_loc'][2]['value']
                                    )
            newspage.send_keys_(ele6,'12345@qq.com')
            ele7=newspage.find_element_(
                self.data['regular_member']['msn_loc'][1]['type'],
                self.data['regular_member']['msn_loc'][2]['value']
                                    )
            newspage.send_keys_(ele7,'12323@msn.com')
            ele8=newspage.find_element_(
                self.data['regular_member']['tel_loc'][1]['type'],
                self.data['regular_member']['tel_loc'][2]['value']
                                    )
            newspage.send_keys_(ele8,'15621312123')
            ele9=newspage.find_element_(
                self.data['regular_member']['ip_loc'][1]['type'],
                self.data['regular_member']['ip_loc'][2]['value']
                                    )
            newspage.send_keys_(ele9,'192.168.2.11')
            ele10=newspage.find_element_(
                self.data['regular_member']['head_portrait'][1]['type'],
                self.data['regular_member']['head_portrait'][2]['value']
                        )
            newspage.send_keys_(ele10,self.data['regular_member']['head_img'][2]['value'])
            ele11=newspage.find_element_(
                self.data['regular_member']['address'][1]['type'],
                self.data['regular_member']['address'][2]['value']
            )
            newspage.send_keys_(ele11,'南京市江宁双龙大道')

            ele12=newspage.find_element_(
                self.data['regular_member']['zip_code'][1]['type'],
                self.data['regular_member']['zip_code'][2]['value']
            )
            newspage.send_keys_(ele12,'212404')

            ele13 = newspage.find_element_(
                self.data['regular_member']['personal'][1]['type'],
                self.data['regular_member']['personal'][2]['value']
            )
            newspage.send_keys_(ele13, '这是我的个人简介')

            ele14 = newspage.find_element_(
                self.data['regular_member']['register'][1]['type'],
                self.data['regular_member']['register'][2]['value']
            )
            newspage.click_(ele14)
            newspage.wait_title('会员中心')
            title=newspage.title_()
            self.assertEqual(title,self.data['regular_member']['check_regular'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test regular member register is end")
            newspage.quit_browser_()
    #企业会员注册
    def test_corporate_register(self):#企业会员注册成功测试用例
        self.logger.info("Start test corporate member register")
        driver=browser()
        newspage = Register(driver)
        newspage.open_browser_()
        newspage.load_member_center()
        newspage.load_corporate_member()
        try:
            ele1=newspage.find_element_(
                self.data['corporate_member']['username_loc'][1]['type'],
                self.data['corporate_member']['username_loc'][2]['value']
            )
            newspage.send_keys_(ele1,get_userNameAndPassword())

            ele2=newspage.find_element_(
                self.data['corporate_member']['password_loc'][1]['type'],
                self.data['corporate_member']['password_loc'][2]['value']
            )
            newspage.send_keys_(ele2,'123456')

            ele3=newspage.find_element_(
                self.data['corporate_member']['repassword_loc'][1]['type'],
                self.data['corporate_member']['repassword_loc'][2]['value']
            )
            newspage.send_keys_(ele3,'123456')

            ele4=newspage.find_element_(
                self.data['corporate_member']['email_loc'][1]['type'],
                self.data['corporate_member']['email_loc'][2]['value']
            )
            newspage.send_keys_(ele4,get_Email())

            ele5=newspage.find_element_(
                self.data['corporate_member']['company_loc'][1]['type'],
                self.data['corporate_member']['company_loc'][2]['value']
                        )
            newspage.send_keys_(ele5,'江苏神州信源')
            ele6=newspage.find_element_(
                self.data['corporate_member']['truename_loc'][1]['type'],
                self.data['corporate_member']['truename_loc'][2]['value']
                                    )
            newspage.send_keys_(ele6,'王治本')
            ele7=newspage.find_element_(
                self.data['corporate_member']['telname_loc'][1]['type'],
                self.data['corporate_member']['telname_loc'][2]['value']
                                    )
            newspage.send_keys_(ele7,'王导')

            ele8=newspage.find_element_(
                self.data['corporate_member']['tel_loc'][1]['type'],
                self.data['corporate_member']['tel_loc'][2]['value']
                                    )
            newspage.send_keys_(ele8,'1543123123')

            ele9=newspage.find_element_(
                self.data['corporate_member']['fax_loc'][1]['type'],
                self.data['corporate_member']['fax_loc'][2]['value']
                                    )
            newspage.send_keys_(ele9, '41231')

            ele10=newspage.find_element_(
                self.data['corporate_member']['qq_loc'][1]['type'],
                self.data['corporate_member']['qq_loc'][2]['value']
                                    )
            newspage.send_keys_(ele10,'12345312')

            ele11=newspage.find_element_(
                self.data['corporate_member']['msn_loc'][1]['type'],
                self.data['corporate_member']['msn_loc'][2]['value']
                                    )
            newspage.send_keys_(ele11,'12323@msn.com')

            ele12=newspage.find_element_(
                self.data['corporate_member']['ip_loc'][1]['type'],
                self.data['corporate_member']['ip_loc'][2]['value']
                                    )
            newspage.send_keys_(ele12,'192.168.3.32')

            ele13=newspage.find_element_(
                self.data['corporate_member']['head_portrait'][1]['type'],
                self.data['corporate_member']['head_portrait'][2]['value']
                        )
            newspage.send_keys_(ele13,self.data['regular_member']['head_img'][2]['value'])

            ele14=newspage.find_element_(
                self.data['corporate_member']['address'][1]['type'],
                self.data['corporate_member']['address'][2]['value']
            )
            newspage.send_keys_(ele14,'南京市江宁双龙大道')


            ele15=newspage.find_element_(
                self.data['corporate_member']['zip_code'][1]['type'],
                self.data['corporate_member']['zip_code'][2]['value']
            )
            newspage.send_keys_(ele15,'212404')

            ele16 = newspage.find_element_(
                self.data['corporate_member']['personal'][1]['type'],
                self.data['corporate_member']['personal'][2]['value']
            )
            newspage.send_keys_(ele16, '这是我的个人简介')

            ele17 = newspage.find_element_(
                self.data['corporate_member']['register'][1]['type'],
                self.data['corporate_member']['register'][2]['value']
            )
            newspage.click_(ele17)
            newspage.wait_title('会员中心')
            title=newspage.title_()
            self.assertEqual(title,self.data['regular_member']['check_regular'][2]['value'])
        except Exception as msg:
            self.logger.error(msg)
            newspage.quit_browser_()
        finally:
            self.logger.info("test regular member register is end")
            newspage.quit_browser_()

if __name__ == '__main__':
    unittest.main()

