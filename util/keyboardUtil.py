# -*- coding:UTF-8 -*-
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
#
#
#
# class Keys_action():
#     def __init__(self,driver,element):
#         self.driver=driver
#         self.element=element
#
#     def enter(self):
#         ActionChains(self.driver).key_down(Keys.ENTER, self.element).key_up(Keys.ENTER).perform()
#
#     def shift(self):
#         ActionChains(self.driver).key_down(Keys.SHIFT, self.element).key_up(Keys.SHIFT).perform()
#
#     def ctrla(self):
#         ActionChains(self.driver).key_down(Keys.CONTROL, self.element).send_keys('a').key_up(Keys.ENTER).perform()
#
#     def ctrlc(self):
#         ActionChains(self.driver).key_down(Keys.CONTROL, self.element).send_keys('c').key_up(Keys.ENTER).perform()
#
#     def ctrlv(self):
#         ActionChains(self.driver).key_down(Keys.CONTROL, self.element).send_keys('v').key_up(Keys.ENTER).perform()