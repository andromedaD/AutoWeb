from selenium import webdriver
from time import sleep
from testdata import *
driver=webdriver.Firefox()
driver.get('http://localhost')
sleep(2)
driver.switch_to.alert
# driver.find_element(By.LINK_TEXT,"新闻中心").click()
# element_loc=(testDataInfo()["element_loc"]["type"],testDataInfo()["element_loc"]['value'])
# print(element_loc)
# driver.find_element(element_loc)
# print(element_loc)
# driver.find_element()
# print(type(element_loc))
# driver.find_element_by_name('username').send_keys('wangjin')
# driver.find_element_by_name('password').send_keys('123456')
# driver.find_element_by_name('Submit').click()
# sleep(3)
# text=driver.find_element_by_link_text('我的空间').text
# print(text)
# driver.find_element_by_name('Submit2').click()
# driver.current_window_handle()
# driver.switch_to.window()
# import pymysql
# #打开数据库
# db=pymysql.connect("localhost",'root','','empirecms')
# #使用cursor()方法创建游标对象
# cursor=db.cursor()
# #使用execute方法执行SQL查询
# cursor.execute("SELECT VERSION()")
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)
# # # 使用 execute() 方法执行 SQL，如果表存在则删除
# # cursor.execute("DROP TABLE IF EXISTS bbk")
# # #创建数据库表sql语句
# # sql="""CREATE TABLE bbk(
# #     FIRST_NAME CHAR(20) NOT NULL,
# #     LAST_NAME CHAR(20),
# #     AGE INT,
# #     SEX CHAR(1),
# #     INCOME FLOAT)
# #     """
# username='wangjin'
# sql="select * from phome_enewsmember where username like %s "%(username)
# cursor.execute(sql)
# results=cursor.fetchall()
# print(results)
#
# # 关闭数据库连接
# # db.close()
# for a in range(4):
#     print(a)











