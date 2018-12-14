# -*- coding:UTF-8 -*-
import yaml
def testDataInfo():
    '''测试数据'''
    with open(r'D:\AutoWeb\test_data\testdata','rb') as fb:
        fb_stream=fb.read()
        testdata_info=yaml.load(fb_stream)
        fb.close()
    return testdata_info

if __name__ == '__main__':
    datas=testDataInfo()
    for key,value in datas.items():
        print(key,':',value)