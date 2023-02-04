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
    # ����
    def start(self):
        data = YamlInfo.read_info()
        if self.driver is None:
            logging.info(f"driverΪ:{self.driver}")
            # ��ʼ����������Ӧ��
            self.desired_caps = data.get('mulatorsetcaps')
            address_set = data.get('addressset')[0]

            # �ͻ��˺ͷ���˽�������
            self.driver = webdriver.Remote(address_set, self.desired_caps)
            # ��ʽ�ȴ���ÿһ�β���Ԫ�ص�ʱ�򣬶�̬����
            self.driver.implicitly_wait(10)
        else:
            # ����app
            logging.info(f"���� driver .")
            self.driver.start_activity(app_package=data['mulatorsetcaps']['appPackage'],
                                       app_activity=data['mulatorsetcaps']['appActivity'])
        return self

    # ֹͣ
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
