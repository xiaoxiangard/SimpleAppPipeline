# -*- coding: GBK -*-
# -*- coding: UTF-8 -*-
# coding=gbk
"""
__author__: wangxiaoxiang
"""
import yaml


# ����yaml����
class YamlInfo:

    # �����෽����������ȥʵ����
    @classmethod
    def read_info(cls):
        # ��ȡyaml����,�ж��ĸ�����
        with open('../Data/nox.yaml', 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        return data
