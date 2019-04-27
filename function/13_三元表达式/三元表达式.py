#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 三元表达式
    @Author: changchun_wu
    @Date: 2019/4/14 21:55
    @Version: 1.0 
"""

name = 'alex1'
test = 'SB' if name == 'alex' else '帅哥'
print(test)

# 列表解析
li = ['鸡蛋%s' % i for i in range(10)]
print(li)

li = ['鸡蛋%s' % i for i in range(10) if i > 2 and i < 7]
print(li)
