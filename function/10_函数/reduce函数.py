#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: reduce函数
    @Author: changchun_wu
    @Date: 2019/4/8 15:41
    @Version: 1.0 
"""

# num_l = [1, 2, 4, 5, 7]
# def add(array):
#     sum_num = 0
#     for i in array:
#         sum_num = sum_num + i
#     return sum_num
#
# print(add(num_l))
from functools import reduce


def add(num, sum_num):
    return num * sum_num


num_l = [1, 2, 5, 5]


def reduce_test(func, array, init=None):
    if init is None:
        sum_num = array.pop(0)
    else:
        sum_num = array.pop(0) * init
    for i in array:
        sum_num = func(i, sum_num)
    return sum_num


print(reduce_test(lambda x, y: x * y, num_l, 100))

### 处理一个列表,对列表中的元素进行合并操作
print(reduce(lambda x, y: x * y, num_l, 100))

