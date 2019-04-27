#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 字符串2
    @Author: changchun_wu
    @Date: 2019/3/26 23:38
    @Version: 1.0 
"""

# 索引
print('取索引')
test = 'admin'
print(test[1])  # 取指定索引的字符
print('------------------------------')

# 切片
print('切片')
print(test[0:2])  # 取指定索引范围的字符(半开区间)
print(test[1:-1])  # -1指到最后的位置(不包含最后的字符)
print('------------------------------')

# 取字符串长度---len()
test = 'admin'
print('取字符串长度---len()')
print(len(test))  # 取字符串的长度
print(test.__len__())  # 取字符串的长度
print('------------------------------')

# 创建连续/不连续数字---range()
print('创建连续数字---range()')
print(range(3))  # [0,3)
print(range(1, 4))  # [1,4)
test = range(1, 10, 2)  # 设置步长指定不连续
for item in test:
    print(item)
print('------------------------------')

# for循环
print('for循环')
test = '你好啊'
for item in test:
    print(item)

for index, item in enumerate(test):
    print(index, item)
print('------------------------------')
# 练习
test = 'hello'
index = 0
while index < len(test):
    print(test[index])
    index += 1

