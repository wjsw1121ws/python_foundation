#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 全局变量
    @Author: changchun_wu
    @Date: 2019/4/2 10:53
    @Version: 1.0 
"""

##########全局变量
# 全局变量没有缩进, 在函数外面定义
# 全局变量作用于整个类

##########局部变量
# 局部变量定义在函数(方法)中
# 局部变量只作用于函数(方法)中
# 可以通过global关键字在函数(方法)中声明全局变量
# 可以在内部内中通过nonlocal关键字修改外部类的变量

##########命名规范
# 全局变量变量名全部大写
# 局部变量变量名全部小写

##########
# 对于嵌套的函数, 内部的函数输在执行时,
# 如果参数在该层函数中未定义, 则从紧挨着的一层获取,
# 如果还是找不到则去外层的外层找,实在找不到再找全局

# 全局变量
NAME = 'alex'


def change_name():
    # 局部变量
    name = 'tina'
    print(name)


change_name()
print(NAME)


def change_name1():
    # 在函数(方法)中定义全局变量
    global NAME
    NAME = 'tina'
    print(NAME)


change_name1()
print(NAME)

# 可以通过global关键字在函数(方法)中声明全局变量#########
name = '刚娘'


def wei():
    name = '陈卓'

    def weiwei():
        global name
        name = '冷静'

    weiwei()
    print(name)


print(name)
wei()
print(name)

# 可以在内部内中通过nonlocal关键字修改外部类的变量
name = '刚娘'


def wei():
    name = '陈卓'

    def weiwei():
        nonlocal name
        name = '冷静'

    weiwei()
    print(name)


print(name)
wei()
print(name)

# 对于嵌套的函数, 内部的函数输在执行时,
# 如果参数在该层函数中未定义, 则从紧挨着的一层获取,
# 如果还是找不到则去外层的外层找,实在找不到再找全局
name = 'haimeng'


def aa():
    name = 'sisi'

    def bb():
        print(name)

    bb()


aa()
