# -*- coding:UTF-8 -*-
import os
import time
import smtplib
import unittest
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from BSTestRunner import BSTestRunner
from config import *

def send_mail(latest_report):#发送带附件测试邮件
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()
    # print(mail_content)
    config_info=configInfo()
   
    smtpserver=config_info['EMAIL']['smtpserver']
    user=config_info['EMAIL']['user']
    password=config_info['EMAIL']['password']
    sender=config_info['EMAIL']['sender']
    recives=config_info['EMAIL']['recives']
    subject=config_info['EMAIL']['subject']


    emailpart_path=r'D:\python_script\image\test.jpg'
    send_file = open(emailpart_path, 'rb').read()#发送文件路径
    att = MIMEText(send_file, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attchment;filename="test.jpg"'
    #装载附件
    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msgRoot['Subject'] = subject
    msgRoot['From'] =user
    msgRoot['To'] = ','.join(recives)
    msgRoot.attach(att)
    #发送邮件
    print("Start Send Email")
    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, recives, msgRoot.as_string())
    print("Send Email is over!!!")
    smtp.close()

def latest_report(report_dir):#返回最后的测试报告
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("the latest report is" + lists[-1])
    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file

if __name__ == '__main__':
    config_info = configInfo()
    case_dir = config_info['case_dir']
    report_dir = config_info['report_dir']
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')
    report_time=time.strftime("%Y-%m-%d %H_%M_%S")
    report_path=report_dir+'/'+report_time+"result.html"
    try:
        with open(report_path,'wb') as fb:
            runner=BSTestRunner(
                stream=fb,title='test report',description='this is baidu test report'
            )
            runner.run(discover)
    finally:
        fb.close()

    latest_report=latest_report(report_dir)
    send_mail(latest_report)
