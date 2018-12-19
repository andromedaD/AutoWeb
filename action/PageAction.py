# -*- coding:UTF-8 -*-

import os
import time
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.config import *
class Page():
    '''页面操作，如click_、find_element_，简单封装方法，以便维护'''
    def __init__(self,driver):
        config_info=configInfo()
        self.driver=driver
        self.base_url=config_info['base_url']
    #私有方法供open_broswer_()使用
    def _open(self,url):
        new_url=self.base_url+url
        self.driver.get(new_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    #打开网页，如打开百度
    def open_browser_(self):
        self._open(self.url)
        # sleep(2)
    #关闭浏览器
    def quit_browser_(self):#退出网页
        self.driver.quit()
        sleep(2)
    # 返回标签文本，一般用于link_text
    def text_(self,element):
        return element.text
    #返回title
    def title_(self):
        return self.driver.title
    # 因为tag_name不实用，所以去除了
    def find_element_(self,type,*element_loc):
        if type=="id":
            el=self.driver.find_element_by_id(*element_loc)
            return el
        elif type=="name":
            el = self.driver.find_element_by_name(*element_loc)
            return el
        elif type=="xpath":
            el=self.driver.find_element_by_xpath(*element_loc)
            return el
        elif type=="css":
            el = self.driver.find_element_by_css_selector(*element_loc)
            return el
        elif type=="link_text":
            el = self.driver.find_element_by_link_text(*element_loc)
            return el
        elif type=="partial_link_text":
            el = self.driver.find_element_by_partial_link_text(*element_loc)
            return el
        else:
            raise NameError("Please enter a valid type of targeting elements.")
    ##因为tag_name不实用，所以去除了
    def find_elements_(self,type,*element_loc):
        if type=="id":
            el=self.driver.find_elements_by_id(*element_loc)
            return el
        elif type=="name":
            el = self.driver.find_elements_by_name(*element_loc)
            return el
        elif type=="xpath":
            el=self.driver.find_elements_by_xpath(*element_loc)
            return el
        elif type=="css":
            el = self.driver.find_elements_by_css_selector(*element_loc)
            return el
        elif type=="link_text":
            el = self.driver.find_elements_by_link_text(*element_loc)
            return el
        elif type=="partial_link_text":
            el = self.driver.find_elements_by_partial_link_text(*element_loc)
            return el
        else:
            raise NameError("Please enter a valid type of targeting elements.")
    #根据标签定位返回，属性的值
    def get_attribute_(self,el,content):
        return el.get_attribute(content)
    '''
    用法如：el=newspage.find_element_("id","...")
           att=get_attribute(el,"href")返回网址的具体值
           newspage已经有driver
    '''
    #鼠标点击，入参为如driver.find_element_by_id("kw")
    def click_(self,element):#点击操作
        element.click()
        sleep(2)
    # 弹窗确认
    def accept_(self):
        self.driver.switch_to.alert.accept()
        sleep(2)
    # 弹窗取消
    def dismiss_(self):
        self.driver.switch_to.alert.dismiss()
        sleep(2)
    # 浏览器前进
    def forward_(self):
        self.driver.forward()
    # 浏览器后退
    def back_up_(self):
        self.driver.back()
    # 发送文本
    def send_keys_(self,element,content):
        element.send_keys(content)
        sleep(1)
    # 清除标签文本内容，入参为如driver.find_element_by_id("kw")
    def clear_(self,element):
        element.clear()
        sleep(1)
    #显示等待10，知道出现想要的title
    def wait_title(self,title):
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))
    # 显示等待10，知道出现想要的定位可见
    def wait_ele(self,type,element_loc):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.find_element_(type,element_loc)))
    # 用于点击后页面跳转至新网页，通过获取handle[-1]的值切换对应窗口
    def switch_new_window_(self):
        handlers=self.driver.window_handles
        self.driver.switch_to.window(handlers[-1])
    #进入嵌套iframe
    def switch_to_frame_(self,tag_name,num):
        if num.isdigit():
            try:
                self.driver.switch_to.frame(
                    self.driver.find_elements_by_tag_name(tag_name)[num]
                )
            except:
                raise TypeError("please check you tag_name or num")
                #t退出嵌套iframe
    def swicth_to_default_content_(self):
        self.driver.switch_to.default_content()
    # 截图
    def insert_img(self):
        filename=time.strftime("%Y-%m-%d %H_%M_%S")+'.jpg'
        filepath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/test_report/image/'+filename
        self.driver.get_screenshot_as_file(filepath)




