# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging
import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from BasePages.base_page import BasePage
from Utils.yaml_info import YamlInfo
timeout = 30
poll = 2


class App(BasePage):
    # 启动
    def start(self):
        data = YamlInfo.read_info()
        if self.driver is None:
            logging.info(f"driver为:{self.driver}")
            # 初始化操作：打开应用
            self.desired_caps = data.get('mulatorsetcaps')
            address_set = data.get('addressset')[0]

            # 客户端和服务端建立连接
            self.driver = webdriver.Remote(address_set, self.desired_caps)
            # 隐式等待，每一次查找元素的时候，动态查找
            self.driver.implicitly_wait(10)
        else:
            # 启动app
            logging.info(f"复用 driver .")
            self.driver.start_activity(app_package=data['mulatorsetcaps']['appPackage'],
                                       app_activity=data['mulatorsetcaps']['appActivity'])
        return self

    # 停止
    def stop(self):
        self.driver.quit()

    def is_record_event_btn_exist(self):
        elem = self._find_elem_by_xpath('//android.widget.Button[contains(@resource-id,"id/trackEventButton")]')
        return elem is not None

    def _find_elem_by_xpath(self, elem_xpath, time_out=timeout, raise_exception=True):
        start = time.time()
        elem = None
        while time.time() - start < time_out and elem is None:
            time.sleep(poll)
            try:
                elem = self.find(MobileBy.XPATH, elem_xpath)
            except Exception:
                print('by pass the element not found')

        if elem is None and raise_exception:
            raise LookupError(f'The element which xpath is {elem_xpath} could not be found')

        return elem
