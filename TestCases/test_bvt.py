# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import logging

from BasePages.app import App


class TestBvt:

    def setup_class(self):
        self.app = App()

    def setup(self):
        self.app.start()

    def teardown_class(self):
        # 关闭app
        self.app.stop()

    def test_bvt(self):
        logging.info("BVT test is started!")
        result = self.app.is_record_event_btn_exist()
        logging.info(f"The record event button is exist - {result}")
        assert result

