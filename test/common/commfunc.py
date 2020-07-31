# -*-coding:utf-8-*-


import os
from utils.logUtil import Log

logger = Log()


def ping(ip='www.baidu.com'):
    '''判断网络连通情况'''
    result = os.system('ping -n 5 -w 1000 %s' % ip)  # 实现pingIP地址的功能,windows命令
    # result = os.system('ping -n 3 -w 1000 192.168.16.1')
    if result:
        logger.info('ping %s fail' % ip)
    else:
        # print('ping %s OK' % ip)
        logger.info('ping %s OK' % ip)
    # print(result)
    return result


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import os
import random


def get_randomIP(ip, count=244):
    """简单获取地址池11-254的随机IP
    :param ip: 起始IP地址
    :param count: 可用IP地址个数
    :return: 随机取出的IP地址
    """

    ip = ip.split('.')
    IP_list = []
    for i in range(0, int(count)):
        IP_end = int(ip[-1]) + i
        if 11 <= IP_end <= 254:
            IP_list.append('%s.%s.%s.%s' % (ip[0], ip[1], ip[2], str(IP_end)))
        else:
            print("please check param")
    IP_new = random.choice(IP_list)
    return IP_new


if __name__ == '__main__':
    ping()
    get_randomIP("192.168.1.11")

