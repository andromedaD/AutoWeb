# -*- coding:UTF-8 -*-
import yaml
def configInfo():
    '''读取config配置文件，返回字典类型'''
    with open(r'D:\AutoWeb\conf\config.yaml','rb') as fb:
        fb_stream=fb.read()
        config_info=yaml.load(fb_stream)
        fb.close()
    return config_info

if __name__ == '__main__':
    print(type(configInfo()))
