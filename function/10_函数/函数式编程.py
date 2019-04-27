#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 函数式编程
    @Author: changchun_wu
    @Date: 2019/4/4 0:36
    @Version: 1.0 
"""


##########高阶函数
# 函数接收的参数是一个函数名
# 返回值中包含函数


def aa():
    print('from aa')


def bb():
    print('from bb')
    return aa


cc = bb()
cc()
print('---------------\n')


def mm():
    print('from mm')

    def nn():
        print('from nn')

    return nn


gg = mm()
gg()
print('---------------\n')


def handle():
    print('from handle')
    return handle


haha = handle()
haha()
print('---------------\n')


def test1():
    print('from test1')


def test2():
    print('from test2')
    return test1()


test2()

print('---------------\n')


def kk1():
    print('from kk1')


def kk2(x):
    print('from kk2')
    return x


kk2(kk1())
print('---------------\n')


def hh1():
    print('from hh1')


def hh2(x):
    print('from hh2')
    return x


hh = hh2(hh1)
hh()
print('---------------\n')

########尾递归调用

# 非尾递归调用

def ee1(x):
    return ee1(x * 2 + 1)
    print('from ee1')

# 尾递归调用
def ee2(x):
    print('from ee2')
    return ee2(x*2+1)
