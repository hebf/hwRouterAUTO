#!/usr/bin/env python
# -*- coding: utf-8 -*-

from poium import Page
from poium import NewPageElement as PageElement


class LoginPage(Page):
    passwd_input = PageElement(xpath="//*[@id='userpassword_ctrl']", describe="密码输入框")
    login_button = PageElement(xpath="//*[@id='loginbtn']", describe="登陆框")
