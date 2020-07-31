# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Email  : hebovan@live.com
# @Author : hbf


from time import sleep
from utils.logUtil import Log
# from test.common.browser import Browser
from selenium import webdriver
from page.mywifi_page import MywifiPage
from page.login_page import LoginPage

logger = Log()


# assertion = YamlConfig(CONFIG_FILE).get("assertion")


class TestMywifi(object):
    """测试我的Wi-Fi,更改SSID，密码字符
    前置条件：向导设置完成，双频优选关闭，取消勾选"将 Wi-Fi 密码作为路由器登录密码"
    """

    def test_ssid_passwd(self):
        url = "http://192.168.3.1"  #路由器管理IP
        passwd = "12345678"         #登录密码
        ssid2g = "hilink_test"
        ssid5g = "hilink_test_5g"
        passwd2g = "012345678901234567890123456789012345678901234567890123456789012"
        passwd5g = "012345678901234567890123456789012345678901234567890123456789012"
        assertion = "华为路由WS5200 增强版"

        # +++++++++++++++++++++++++++++登陆设备+++++++++++++++++++
        driver = webdriver.Chrome()
        driver.maximize_window()
        page = LoginPage(driver)
        page.get(url)
        page.passwd_input.send_keys(passwd)
        page.login_button.click()
        assert driver.title == assertion
        logger.info("页面标题是：%s" % (driver.title))
        # +++++++++++++++++++++++++++配置WIFI++++++++++++++++
        page = MywifiPage(driver)
        page.main_menu_button.click()
        page.name2g_input.clear()
        page.name2g_input.send_keys(ssid2g)
        page.passwd2g_input.send_keys(passwd2g)
        # page.check_old_passwd.send_keys(passwd)
        page.name5g_input.clear()
        page.name5g_input.send_keys(ssid5g)
        page.passwd5g_input.send_keys(passwd5g)
        page.save_button.click()
        sleep(10)
        driver.close()
        print("2.4g和5g无线配置完成，终端连接确认配置是否生效")

if __name__ == "__main__":
    TestMywifi().test_ssid_passwd()