# -*- coding:UTF-8 -*-
from selenium import webdriver
from time import sleep
def browser():
    '''获取浏览器驱动'''
    # driver=webdriver.Firefox()
    #driver=webdriver.Chrome()
    # driver=webdriver.Ie()
    driver=webdriver.PhantomJS()
    return driver