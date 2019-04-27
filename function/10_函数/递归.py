#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 递归
    @Author: changchun_wu
    @Date: 2019/4/3 16:05
    @Version: 1.0 
"""


########递归的特征
# 必须有一个明确是结束条件

def digui(x):
    print(x)
    if int(x / 2) == 0:
        return x
    return digui(int(x / 2))


digui(10)

##########
person = ['alex', 'allen', 'json', 'john']


def ask_way(person_list):
    if len(person_list) == 0:
        return '没人知道路'
    if person_list[0] == 'json':
        return '问到路了'
    person_list.pop(0)
    return ask_way(person_list)

print(ask_way(person))
