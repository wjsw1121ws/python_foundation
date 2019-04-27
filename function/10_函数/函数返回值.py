#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 函数的返回值
    @ClassName: 函数的返回值
    @Author: changchun_wu
    @Date: 2019/4/1 23:21
    @Version: 1.0 
"""


######################
# 函数走到return就结束运行
# 没有返回值返回       --->None
# 有一个返回值返回     --->Object
# 有多个返回值        --->返回元组

def test01():
    """
    没有返回值
    """
    x = 2
    y = 2 * x + 1


print(test01())


def test02(x):
    """
    有一个返回值
    :param x: 传入参数
    :return: 返回值
    """
    y = 2 * x + 1
    return y


print(test02(3))


def test03(x, y):
    """
    有多个返回值
    :param x:
    :param y:
    :return:
    """
    z = x + y
    return x, y, z


print(test03(2, 3))
