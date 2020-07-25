#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 10:01
# @Version : 1.0
# @File    : win_clock.py
# @Author  : Jingsheng Tang
# @Version : 1.0
# @Contact : mrtang@nudt.edu.cn   mrtang_cs@163.com
# @License : (C) All Rights Reserved


u'''
windows下通过queryperformance提供微妙级别计时
'''

from __future__ import division
import ctypes

try:
    import platform
    if platform.system().lower() != 'windows':
        raise Exception('[Info] unsupported platform')
except:
    raise Exception('[Info] unsupported platform')

kernel32dll = ctypes.windll.kernel32
#kernel32dll.SetThreadAffinityMask(kernel32dll.GetCurrentThread(),0x00000001)
freq = ctypes.c_longlong(0)
kernel32dll.QueryPerformanceFrequency(ctypes.byref(freq))
freq = freq.value

def timeclock():
    counter  = ctypes.c_longlong(0)
    kernel32dll.QueryPerformanceCounter(ctypes.byref(counter))
    return counter.value/freq
