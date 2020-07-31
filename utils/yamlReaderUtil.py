# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   : 5/11/2020 10:09 AM
# @email  : hebovan@live.com
# @Author : hbf

import os
import yaml

"""
读取yaml文件
"""

class YamlReader(object):
    def __init__(self, yamlfile):
        if os.path.exists(yamlfile):
            self.yamlf = yamlfile
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 读取yaml数据，并转换为列表
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class YamlConfig(object):
    def __init__(self, yamlfile):
        self.conf = YamlReader(yamlfile).data

    def get(self, element, index = 0):
        """
        yaml在由多个文档合并组成时，使用‘---’作为分隔，传入index来获取。
        """
        return self.conf[index].get(element)


# if __name__ == '__main__':
#     ya = YamlConfig('G:/python_git_star/apiAUTO/config/config.yaml')
#     print(ya.get('CLIENT_INFO'))