#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: mr tang
# Date:   2018-11-02 22:33:56
# Contact: mrtang@nudt.edu.cn
# Last Modified by:   mr tang
# Last Modified time: 2018-11-05 22:43:39
# Last Modified time: 2020-02-04

u'''
该脚本用于提供亚毫秒甚至微妙级别的计时功能。在linux系统下，gettimeofday具有
提供微妙级精度的计时函数。经过测试和阅读文档，python中的内置函数datetime.datetime
以及time.time的实现正是基于gettimeofday。因此本脚本将直接使用datetime.datetime。
'''

try:
    import platform
    if platform.system().lower() != 'linux':
        raise(Exception('[Info] unsupported platform'))
except:
    raise(Exception('[Info] unsupported platform'))

import datetime

class LinuxTime():
    def __init__(self):
        self.time = datetime.datetime.now()

    def now(self):
        self.time = datetime.datetime.now()
        # return self.time

    def timestamp(self):
        return self.time.timestamp()

    def formatstring(self):
        return str(self.time)

    def __sub__(self, other):
        return self.time.timestamp() - other.time.timestamp()


    
    
    
    
    
    
    
    
    