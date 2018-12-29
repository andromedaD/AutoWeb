# -*- coding: utf-8 -*-
'''
@File  : requests.py
@Author: 王治本
@Contact : 568898699@qq.com
@Date  : 2018/12/21 0021 17:32
'''

import requests
import json
import os
from requests.auth import HTTPBasicAuth
# r=requests.post('http://api.github.com/some/endpoint',data=json.dumps({'some':'data'}))
# print(r.json())

# data={'some':'data'}
# headers={'content-type':'application/json',
#          'User-Aagent': 'Mozzilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
#
# r=requests.post('http://api.github.com/some/endpoint',data=data,headers=headers)
# print(r.text)

# r=requests.get('http://www.itwhy.org')
# print(r.content)
# # print(r.text,'\n{}\n'.format('*'*79),r.encoding)
# # r.encoding='GBK'
# # print(r.text,'\n{}\n'.format('*'*79),r.encoding)

# URL='http;//ip.taobao.com/service/getIpInfo.php'
# try:
#     r=requests.get(URL,params={'ip':'8.8.8.8'},timeout=1)
#     r.raise_for_status()
# except requests.RequestException as e:
#     print(e)
# else:
#     result=r.json()
#     print(type(result),result,sep='\n')
# filepath=os.path.dirname(os.path.dirname(__file__))+'/test_report/image/test.jpg'
# # print(os.path.isfile(filepath))
# url='http://127.0.0.1:5000/upload'
# files={'file':open(filepath,'rb')}
#
# r=requests.post(url,files=files)
# print(r.text)

# r = requests.get('http://httpbin.org/hidden-basic-auth/user/passwd',
#                  auth=HTTPBasicAuth('user','passwd'))
# print(r.json())
# r=requests.get('http://www.baidu.com')
# print(r.cookies['BDORZ'])
# print(tuple(r.cookies))

# url = 'http://httpbin.org/cookies'
# cookies={'testcookies_1':'Hello_python3','test_cookies_2':'Hello_Requests'}
# r=requests.get(url,cookies=cookies)
# print(r.json())

#
# headers={
#     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Encoding':'gzip,deflate,compress',
#     'Accept-Language':'en-us,q=0.5,en;q=0.3',
#     'Cache-Control':'max-age=0',
#     'Connection':'keep-alive',
#     'User-Agent':'Mozilla/5.0 (X11;Ubuntu;Linux x86_64;rv:22.0)\
#     Gecko/20100101 Firefox/22.0'
# }
#
# s=requests.Session()
# s.headers.update(headers)
# s.get('http://www.kuaipan.cn/account_login.htm')
# _URL='http://www.kuaipan.cn/index.php'
# s.post(_URL,params={'ac':'account','op':'login'},
#        data={'username':'****@foxmail.com','userpwd':'*******','isajax':'yes'})
# r=s.get(_URL,params={'ac':'common','op':'userlogin'})
# print(r.json)
# s.get(_URL,params={'ac':'common','op':'userlogin'})

# res=requests.get('http://www.baidu.com')
# print(res.status_code)
# print(res.headers)
# print(res.encoding)
# print(res.text)
#
#
# payload={'wd':'张澜','rn':'100'}
# r=requests.get('http://www.baidu.com/s',params=payload)
# print(r.url)


#百度地图api接口调用
import json
from urllib.request import urlopen,quote
import requests
import pandas as pd

#读取文件信息
data=pd.read_excel('test_baidumap.xls')
# 构建抓取经纬度函数
def getlnglat(address):
    url='http://api.map.baidu.com/geocoder'
    output='json'
    ak='KFxKtpauFnzGfh8mGwFaej0SNXUDMedI'
    address=quote(address)
    uri=url+'?'+'address='+address+'&output='+output+'&ak='+ak
    req=urlopen(uri)
    res=req.read().decode()
    temp=json.loads(res)
    print(temp)
    lat=temp['result']['location']['lat']
    lng=temp['result']['location']['lng']
    return lat,lng
#抓取经纬度
for indexs in data.index:
    print(indexs)
    get_location=getlnglat(data.loc[indexs,'area'])
    print(get_location)
    get_lat=get_location[0]
    get_lng=get_location[1]
    data.loc[indexs,'纬度']=get_lat
    data.loc[indexs,'经度度']=get_lng

data_html=pd.DataFrame(columns=['content'])

for indexs in data.index:
    data_html.loc[indexs,'content']='{'+\
                                     '"lat:'+str(data.loc[indexs,'纬度'])+','+\
                                     '"lng:'+str(data.loc[indexs,'经度'])+','+\
                                     '"quyu:'+'"'+str(data.loc[indexs,'area'])+'"'+\
                                     '}'+','
data_html.to_csv("data_html.csv",encoding="gbk")










