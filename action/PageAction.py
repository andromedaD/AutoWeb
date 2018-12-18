# -*- coding:UTF-8 -*-

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
    def _open(self,url):
        new_url=self.base_url+url
        self.driver.get(new_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def open_browser_(self):
        self._open(self.url)
        # sleep(2)

    def quit_browser_(self):#退出网页
        self.driver.quit()
        sleep(2)

    def text_(self,element):#elemen为定位元素，如ele1=find_element(By.ID,'username')
        return element.text

    def title_(self):
        return self.driver.title


    def find_element_(self,type,*element_loc):#因为tag_name不实用，所以去除了
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

    def find_elements_(self,type,*element_loc):##因为tag_name不实用，所以去除了
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

    def click_(self,element):#点击操作
        element.click()
        sleep(2)

    def accept_(self):#弹窗确认
        self.driver.switch_to.alert.accept()
        sleep(2)

    def dismiss_(self): #弹窗取消
        self.driver.switch_to.alert.dismiss()
        sleep(2)

    def forward_(self):#浏览器前进
        self.driver.forward()

    def back_up_(self):#浏览器后退
        self.driver.back()

    def send_keys_(self,element,content):#发送文本
        element.send_keys(content)
        sleep(1)

    def clear_(self,element):#清除
        element.clear()
        sleep(1)

    def wait_title(self,title):
        WebDriverWait(self.driver, 10).until(EC.title_contains(title))

    def wait_ele(self,type,element_loc):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(self.find_element_(type,element_loc)))

    def switch_new_window_(self):#用于点击后页面跳转至新网页，通过获取handle[-1]的值切换对应窗口
        handlers=self.driver.window_handles
        self.driver.switch_to.window(handlers[-1])

    def switch_to_frame(self,tag_name,num):
        if num.isdigit():
            try:
                self.driver.switch_to.frame(
                    self.driver.find_elements_by_tag_name(tag_name)[num]
                )
            except:
                raise TypeError("please check you tag_name or num")

    def insert_img(self, filename):#暂时没有想到使用场景，先放着
        # func_path = os.path.dirname(__file__)
        # print(func_path)
        #
        # base_dir = str(func_path)
        # base_dir = base_dir.replace('\\', '/')
        # print(base_dir)
        #
        # base = base_dir.split('/Website')[0]
        # print(base)
        #
        # filepath = base + '/Website/test_report/screenshot' + filename
        filepath=r'D:\AutoWeb\test_report\image\\'+filename
        self.driver.get_screenshot_as_file(filepath)


