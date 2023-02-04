# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # driver: WebDriver ����м�������ע�ͣ������п�������ʹ��
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(f"��λ��:{by}, ��λ���ʽ: {locator}")
        # ����Ԫ��
        return self.driver.find_element(by, locator)
