#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 列表2
    @Author: changchun_wu
    @Date: 2019/3/27 15:33
    @Version: 1.0 
"""

# 索引操作
li = ['aa', 11, 'bb', 22, False, ['cc', 33]]
print('按索引取值')
print(li[5])

print('修改指定索引的元素')
li[1] = 100
print(li)

print('删除指定索引的元素')
del li[0]
print(li)
print('-----------------------------')

# 切片操作
li = ['aa', 11, 'bb', 22, False, ['cc', 33]]
print('取指定切片中的元素')
print(li[1:-1])     #开区间

print('修改指定切片中的元素')
li[1:3] = ['dd']
print(li)

print('删除指定切片中的元素')
del li[1:4]
print(li)
print('-----------------------------')

# 取列表长度
print('取列表长度')
print(len(li))          # 列表是按照数组的每个元素算的
print('------------------------------')

# 判断元素是否在列表中: in
print('判断元素是否在列表中')
li = ['aa', 11, 'bb', 22, False, ['cc', 33]]
var = 'aa' in li
print(var)
print('------------------------------')

# 字符串与列表互转
s = 'admin'
print('字符串转列表')
l = list(s)
print(l)

print('列表转字符串---都由字符串构成的列表')
li=['aa','cc','bb']
v = "".join(li)
print(v)

print('列表转字符串---由不同数据类型构成的列表')
li = ['aa', 11, 'bb', 22, False, ['cc', 33]]
s = ''
for item in li:
    s += str(item)
print(s)
print('------------------------------')

#for循环
for index, item in enumerate(li):
    print(index,item)
