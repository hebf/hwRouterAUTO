# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Email  : hebovan@live.com
# @Author : hbf


from time import sleep

# from test.common.browser import Browser
from selenium import webdriver

from config.globalparam import CONFIG_FILE
from page.login_page import LoginPage
from page.mywifi_page import MywifiPage
from utils.logUtil import Log
from utils.yamlReaderUtil import YamlConfig

logger = Log()


class TestMywifi(object):
    """测试我的Wi-Fi,更改SSID，密码字符
    前置条件：向导设置完成，双频优选关闭，取消勾选"将 Wi-Fi 密码作为路由器登录密码"
    """

    def test_ssid_passwd(self):
        RC = YamlConfig(CONFIG_FILE).get("run_config")
        url = RC.get("url")
        wl = YamlConfig(CONFIG_FILE).get("web_login")
        wificonf = YamlConfig(CONFIG_FILE).get("my_wifi")
        assertion = YamlConfig(CONFIG_FILE).get("assertion")

        # +++++++++++++++++++++++++++++登陆设备+++++++++++++++++++
        driver = webdriver.Chrome()
        driver.maximize_window()
        page = LoginPage(driver)
        page.get(url)
        page.passwd_input.send_keys(wl["password"])
        page.login_button.click()
        assert driver.title == assertion.get("browser_title")
        logger.info("页面标题是：%s" % (driver.title))
        # +++++++++++++++++++++++++++配置WIFI+++++++++++++++
        logger.info("++++++++++++++++++test my_wifi START++++++++++++++++++++++++")
        page = MywifiPage(driver)
        page.main_menu_button.click()
        page.name2g_input.clear()
        page.name2g_input.send_keys(wificonf["ssid2g"])
        page.passwd2g_input.send_keys(wificonf["passwd2g"])
        # page.check_old_passwd.send_keys(passwd)
        page.name5g_input.clear()
        page.name5g_input.send_keys(wificonf["ssid5g"])
        page.passwd5g_input.send_keys(wificonf["passwd5g"])
        page.save_button.click()
        sleep(5)
        driver.close()
        print("2.4g和5g无线配置完成，终端连接确认配置是否生效")
        logger.info("wifi配置如下:\n2.4G SSID: %s,\n2.4G PASSWORD: %s,\n5G SSID: %s,\n5G PASSWORD: %s " %
                    (wificonf["ssid2g"],wificonf["passwd2g"],wificonf["ssid5g"],wificonf["passwd5g"]))


if __name__ == "__main__":
    TestMywifi().test_ssid_passwd()