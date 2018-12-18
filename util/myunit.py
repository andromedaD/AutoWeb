# -*- coding:UTF-8 -*-
# from time import sleep
import unittest


class StartEnd(unittest.TestCase):#unittest初始化
    def setUp(self):
        print("Start test>>>>>>>>>>>>>>>>>>>>")

    def tearDown(self):
        print("End test<<<<<<<<<<<<<<<<<<<<<<")
        # sleep(3)