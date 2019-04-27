#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 函数
    @Author: changchun_wu
    @Date: 2019/4/1 22:55
    @Version: 1.0 
"""

# python中没有类似java方法的重载,
# 当定义的函数名称相同时不管函数的参数是否相同,后写的函数会覆盖之前的函数
def test():
    """
    无参函数的定义
    :return:
    """
    x = 2
    y = 2 * x + 1
    return y
print(test())


def test(x):
    """
    带参函数的定义
    :param x: 传入参数
    :return: 返回值
    """
    y = 2 * x + 1
    return y


print(test(3))