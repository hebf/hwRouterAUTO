# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


#+++++++++配置测试用例运行需要的部分全局变量,开始测试前确认是否需要修改相关值+++++++++++++++++++++++++++++++++++
# BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yaml')
# 日志路径
LOG_PATH = os.path.join(BASE_PATH, 'log')
# 测试报告路径
REPORT_PATH = os.path.join(BASE_PATH, 'report', 'testreport')
# 测试截图路径
IMG_PATH = os.path.join(BASE_PATH, 'report', 'image')
# PC端web测试用例路径
CASE_PATH = os.path.join(BASE_PATH, 'test', 'uitest')




