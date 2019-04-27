#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: map函数
    @Author: changchun_wu
    @Date: 2019/4/4 2:02
    @Version: 1.0 
"""


# lambda x: x + 1
def add_one(x):
    x += 1
    return x


# lambda x: x - 1
def reduce_one(x):
    x -= 1
    return x


def map_test(func, array):
    arr_l = []
    for i in array:
        arr_l.append(func(i))
    return arr_l

arr = [1, 2, 3]
# print(map_test(add_one, array))
print(map_test(lambda x: x + 1, arr))
# print(map_test(reduce_one, array))
print(map_test(lambda x: x - 1, arr))
##############
# print(list(map(add_one, array)))
### 处理列表中的每一个元素, 得到一个新的列表,该列表中的每个元素位置与之前一样
print(list(map(lambda x: x + 1, arr)))
