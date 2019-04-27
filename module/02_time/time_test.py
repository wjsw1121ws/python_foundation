#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: time_test
    @Author: changchun_wu
    @Date: 2019/4/24 23:55
    @Version: 1.0 
"""
import time

if __name__ == '__main__':
    # 返回时间戳
    print(time.time())

    # 结构化时间---local(当地时间)
    print(time.localtime())
    print(time.localtime(time.time()))
    obj = time.localtime()
    print(obj.tm_yday)

    # 结构化时间---UTC(世界标准时间)
    print(time.gmtime())

    # 将结构化时间转化为时间戳
    print(time.mktime(time.localtime()))

    # 将结构化时间转换为字符串时间
    print(time.strftime('%Y-%m-%d %X',time.localtime()))

    # 将字符串时间转化为结构化时间
    print(time.strptime('2019-04-25 00:16:24','%Y-%m-%d %X'))

    # 返回系统时间--字符串时间(通过结构化时间转化而来)
    print(time.asctime())

    # 返回系统时间--字符串时间(通过时间戳转化而来)
    print(time.ctime())

    # 线程推迟指定时间(秒)
    time.sleep(1)

