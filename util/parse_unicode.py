# -*- coding: utf-8 -*-
'''
@File  : parse_unicode.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/21 0021 19:08
'''
import urllib.parse
def build_unicode(args):
    if args:
        try:
            if isinstance(args,str):
                print(args)
                result=urllib.parse.quote(args)
                # print(result)
            elif isinstance(args,list):
                result=[]
                for i in range(len(args)):
                    result.append(urllib.parse.quote(args[i]))
                    # print(result)
        except:
            raise TypeError("type value invaild")
        finally:
            return result
def parse_unicode(args):
    if args:
        try:
            result=urllib.parse.unquote(args)
            print(result)
        except:
            raise TypeError
        finally:
            return result

'''%E4%B8%AD%E5%9B%BD
%E7%BE%8E%E5%9B%BD
%E6%97%A5%E6%9C%AC'''
# args=['中国','美国','日本']
# print(isinstance(args,str))
# build_unicode(args)
# args='%E4%B8%AD%E5%9B%BD'
# result=parse_unicode(args)
# print(result)

