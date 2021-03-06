# -*- coding:UTF-8 -*-
import time
import logging
from os import getcwd
import os
def get_log(logname):
    #创建一个logger
    logger = logging.getLogger(logname)
    logger.setLevel(logging.INFO)

    #设置日志存放路径，日志文件名
    #获取本地实际，转换为设置的格式
    rq = time.strftime('%Y%m%d',time.localtime(time.time()))
    #设置所有日志和错误日志的存放路径
    # path = getcwd()
    #通过文件的绝对路径来拼接日志的存放路径
    all_log_path = r'D:\AutoWeb\test_report\Logs\All_logs\\'
    error_log_path = r'D:\AutoWeb\test_report\Logs\Error_logs\\'

    #设置日志文件名
    all_log_name = all_log_path + rq + '.log'
    error_log_name =error_log_path +rq + '.log'
    #创建handler
    #创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name,encoding='utf-8')
    fh.setLevel(logging.INFO)
    #创建一个handler写入错误日志
    eh = logging.FileHandler(error_log_name,encoding='utf-8')
    eh.setLevel(logging.ERROR)
    #创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    #定义日志输出格式
    #以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    #以时间-日志器名称-日志级别-文件名-函数行数-错误内容
    error_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s -%(lineno)s - %(message)s')
    #将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)
    eh.setFormatter(error_log_formatter)


    #给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(eh)
    logger.addHandler(ch)
    return logger
def log_release():
    logging.shutdown()

get_log('test')