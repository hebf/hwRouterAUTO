#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 6/2/2020
# @email  : hebovan@live.com
# @Author : hbf

import os
from config.globalparam import REPORT_PATH

class Browser(object):
    def __init__(self, seleDriver):
        self.driver = seleDriver

    def capture_screenshots(self, name):
        """
        封装selenium driver截图模块
        :param name: 截图命名
        :return:
        """
        files = os.listdir(REPORT_PATH)
        files.sort()
        file_name = name.split("/")[-1]
        new_report_dir = files[-1]
        if new_report_dir is None:
            raise RuntimeError('没有初始化测试目录')
        image_dir = os.path.join(REPORT_PATH, new_report_dir, "image", file_name)
        self.driver.save_screenshot(image_dir)
