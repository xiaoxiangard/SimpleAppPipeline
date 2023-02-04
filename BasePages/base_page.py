# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # driver: WebDriver 入参中加入类型注释，方法中可以正常使用
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(f"定位符:{by}, 定位表达式: {locator}")
        # 查找元素
        return self.driver.find_element(by, locator)
