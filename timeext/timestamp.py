#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 10:07
# @Version : 1.0
# @File    : timeclock.py
# @Author  : Jingsheng Tang
# @Version : 1.0
# @Contact : mrtang@nudt.edu.cn   mrtang_cs@163.com
# @License : (C) All Rights Reserved


try:
    import platform
    if platform.system().lower() == 'linux':
        from .linuxclock import timeclock
    elif platform.system().lower() == 'windows':
        from .winclock import timeclock
    else:
        raise Exception('[Info] unsupported platform')
except:
    raise Exception('[Info] unsupported platform')

def getstamp():
    return timeclock()
