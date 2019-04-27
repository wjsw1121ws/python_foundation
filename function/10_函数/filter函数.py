#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: filter函数
    @Author: changchun_wu
    @Date: 2019/4/8 15:07
    @Version: 1.0 
"""

# li = ['alex','allen']
# arr = []
#
# def filter_test(array):
#     for i in array:
#         if not i.startswith('ale'):
#             arr.append(i)
#     return arr

# print(filter_test(li))

def start_with(msg):
    return msg.startswith('ale')

li = ['alex','allen']
l2 = []
def filter_test(func,array):
    for i in array:
        if not func(i):
            l2.append(i)
    return l2
# print(filter_test(start_with,li))
print(filter_test(lambda x:x.startswith('ale'),li))
### 遍历列表中的每一个元素并对其进行判断,按照判断结果对列表进行过滤
print(list(filter(lambda x:not x.startswith('ale'),li)))
