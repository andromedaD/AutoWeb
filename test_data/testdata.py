# -*- coding:UTF-8 -*-
import yaml
import os

def testDataInfo(path):
    '''测试数据'''
    curpath=os.path.dirname(os.path.realpath(__file__))
    newpath=os.path.join(curpath,path)
    with open(newpath,'rb',buffering=1024) as fb:
        fb_stream=fb.read()
        testdata_info=yaml.load(fb_stream)
        fb.close()
    return testdata_info

def testdataWrite(path,testdata):
    curpath = os.path.dirname(os.path.realpath(__file__))
    newpath = os.path.join(curpath, path)
    with open(newpath,'a',encoding="utf-8") as fb:
        yaml.dump(testdata,fb)



if __name__ == '__main__':
#     #测试室读取
#     datas=testDataInfo('testdata')
#     for key,value in datas.items():
#         print(key,':',value)
#
#     #测试写入
    testdata={
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'A5RNW18316011440',
        'appPackage': 'com.tencent.mm',
        'appActivity': '.ui.LauncherUI',
        'automationName': 'Uiautomator2',
        'unicodeKeyboard': [True, "hh"],
        'resetKeyboard': True,
    }
    testdataWrite('Login',testdata)
