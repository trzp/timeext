#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 10:01
# @Version : 1.0
# @File    : linux_clock.py
# @Author  : Jingsheng Tang
# @Version : 1.0
# @Contact : mrtang@nudt.edu.cn   mrtang_cs@163.com
# @License : (C) All Rights Reserved


u'''
linux下通过datetime提供高精度计时，其本质是gettimeofday
'''

try:
    import platform
    if platform.system().lower() != 'linux':
        raise(Exception('[Info] unsupported platform'))
except:
    raise(Exception('[Info] unsupported platform'))

import datetime

def timeclock():
    return datetime.datetime.now().timestamp()

