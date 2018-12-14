# -*- coding:UTF-8 -*-
from selenium import webdriver
from time import sleep
def browser():
    '''获取浏览器驱动'''
    driver=webdriver.Firefox()
    #driver=webdriver.Chrome()
    # driver=webdriver.Ie()

    # driver.get("http://www.baidu.com")
    sleep(2)
    return driver