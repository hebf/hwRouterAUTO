#!/usr/bin/env python
# -*- coding: utf-8 -*-

from poium import Page
from poium import NewPageElement as PageElement


class MywifiPage(Page):
    main_menu_button = PageElement(xpath="//*[@id='wifi']/div", describe="我的wifi主菜单")
    name2g_input = PageElement(xpath="//*[@id='content_wifi_name2G_ctrl']", describe="2.4g ssid名称输入框")
    passwd2g_input = PageElement(xpath="//*[@id='content_wifi_password2G_ctrl']", describe="2.4g wifi密码输入框" )
    check_old_passwd = PageElement(xpath="//*[@id='wifi_view_data_edit_oldloginpwd_ctrl']", describe="验证当前登录密码" )
    name5g_input = PageElement(xpath="//*[@id='content_wifi_name5G_ctrl']", describe="5g wifi名称输入框")
    passwd5g_input = PageElement(xpath="//*[@id='content_wifi_password5G_ctrl']", describe="5g wifi密码输入框" )
    save_button = PageElement(xpath="//*[@id='SsidSettings_submitbutton']", describe="保存按钮")