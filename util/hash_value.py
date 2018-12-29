# -*- coding:UTF-8 -*-
import hashlib

# num='123456'
# md5=hashlib.md5()
# md5.update(num.encode('utf-8'))
# result=md5.hexdigest()
# print(result
# )
def hash_md5(num):
    if num:
        md5=hashlib.md5()
        md5.update(num.encode('utf-8'))
        try:
            result=md5.hexdigest()
            print(result)
            return result
        except Exception as msg:
            raise msg
    else:
        raise Exception("Input string %s is invaild"%num)


