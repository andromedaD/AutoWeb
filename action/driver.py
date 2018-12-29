# -*- coding:UTF-8 -*-
from selenium import webdriver
from time import sleep

with open('choose_data','r') as f:
    b=f.read()

def browser(b):
    if b =='firefox':
        driver=webdriver.Firefox()
        return driver
    elif b =='chrome':
        driver=webdriver.Chrome()
        return driver
    elif b =='phantomJS':
        driver=webdriver.PhantomJS()
        return driver
    else:
        print("not match this driver")
#
# def browser():
#     '''获取浏览器驱动'''
#     # driver=webdriver.Firefox()
#     #driver=webdriver.Chrome()
#     # driver=webdriver.Ie()
#     driver=webdriver.PhantomJS()
#     return driver