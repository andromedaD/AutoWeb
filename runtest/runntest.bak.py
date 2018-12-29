# -*- coding:UTF-8 -*-
# import time
# import unittest
# from BSTestRunner import BSTestRunner
from util.send_email import *
from conf.config import *

config_info = configInfo()#全局配置文件
case_dir = config_info['case_dir']#用例路径
report_dir = config_info['report_dir']#测试报告路径
discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py')#测试的具体用例如test_login
report_time = time.strftime("%Y-%m-%d %H_%M_%S")
report_path = report_dir + '/' + report_time + "result.html"#测试报告名称
try:
    with open(report_path, 'wb') as fb:
        runner = BSTestRunner(
            stream=fb, title='test report', description='this is baidu test report'
        )
        runner.run(discover)
except Exception as msg:
    print(msg)
finally:
    fb.close()
#执行测试
latest_report = latest_report(report_dir)
send_mail(latest_report)
