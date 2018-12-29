# -*- coding:UTF-8 -*-
# import time
# import unittest
# from BSTestRunner import BSTestRunner
from util.send_email import *
from conf.config import *
#生成器输出浏览器
def choose_driver():
    L=['firefox','chrome','phantomJS']
    for i in L:
        yield i
def write(choose):
    with open(r'D:\AutoWeb\action\choose_data','w') as fb:
        fb.write(choose)
choose=choose_driver()
#生成firefox
write(next(choose))
config_info = configInfo()#全局配置文件
case_dir = config_info['case_dir']#用例路径
report_dir = config_info['report_dir']#测试报告路径
discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')#测试的具体用例如test_login
report_time = time.strftime("%Y-%m-%d %H_%M_%S")
report_path = report_dir + '/' + report_time + "result.html"#测试报告名称
try:
    with open(report_path, 'wb') as fb:
        runner = BSTestRunner(
            stream=fb, title='test report', description='User-Agent is Mozilla/5.0'
        )
        runner.run(discover)
except Exception as msg:
    print(msg)
finally:
    fb.close()
#执行测试
latest_report = latest_report(report_dir)
send_mail(latest_report)


#选择chrome浏览器
write(next(choose))
discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')#测试的具体用例如test_login
report_time = time.strftime("%Y-%m-%d %H_%M_%S")
report_path = report_dir + '/' + report_time + "result.html"#测试报告名称
try:
    with open(report_path, 'wb') as fb:
        runner = BSTestRunner(
            stream=fb, title='test report', description='User-Agent is Chrome'
        )
        runner.run(discover)
except Exception as msg:
    print(msg)
finally:
    fb.close()
#执行测试
latest_report = latest_report(report_dir)
send_mail(latest_report)

#选择PhantomJS
write(next(choose))
discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')#测试的具体用例如test_login
report_time = time.strftime("%Y-%m-%d %H_%M_%S")
report_path = report_dir + '/' + report_time + "result.html"#测试报告名称
try:
    with open(report_path, 'wb') as fb:
        runner = BSTestRunner(
            stream=fb, title='test report', description='User-Agent is PhantomJS'
        )
        runner.run(discover)
except Exception as msg:
    print(msg)
finally:
    fb.close()
#执行测试
latest_report = latest_report(report_dir)
send_mail(latest_report)

