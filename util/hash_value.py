# -*- coding:UTF-8 -*-
import hashlib
# string = "beyongjie"
# md5 = hashlib.md5()
# md5.update(string.encode('utf-8'))     #注意转码
# res = md5.hexdigest()
# print("md5加密结果:",res)
num='123456'
md5=hashlib.md5()
md5.update(num.encode('utf-8'))
result=md5.hexdigest()
print(result)