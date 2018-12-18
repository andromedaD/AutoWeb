# -*- coding: utf-8 -*-

# @File  : random_user_email.py
# @Author: 王治本
# @Contact : 568898699@qq.com
# @Date  : 2018/12/18 0018 15:10

import random
def get_Email( emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType
    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
        __rang = random.randint(4, 10)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email

def get_userNameAndPassword():
    # 8位用户名及6位密码
    userName = ''.join(
        random.sample("1234567890abcdefghijklmnopqrstuvwxy\
        zABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-><:}{?/", 8)
    )
#   userPassword = ''.join(random.sample("1234567890", 6))
    return userName

if __name__ == '__main__':
    print(get_Email())
    print(get_Email(emailType='@qq.com',rang=20))
    print(get_userNameAndPassword())