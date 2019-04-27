#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: set
    @Author: changchun_wu
    @Date: 2019/3/29 14:45
    @Version: 1.0 
"""

# 由不同元素组成
# 集合无序的
# 集合中的元素必须是不可变类型--->str, int, tuple
set
# 定义集合
s = {1, 'b', ('cc', 4,), 1}
print(s)
print('\n----------------------\n')

# 并集, 差集, 合集
# print('并集, 差集, 合集')
# s1 = {'aa', 11, 'bb', 22}
# s2 = {'aa', 'bb', 'cc', 'dd'}
# print('并集', s1 & s2)
# print('合集', s1 | s2)
# print('差集', (s1 - s2) | (s2 - s1))
# print('\n----------------------\n')

set
# 列表去重
li = ['aaa', 22, 'bbb', 22]
s = set(li)
print(s)
# 设置集合
print('设置集合: set()')
s = set('admin')
s2 = set(['alex', 'allen'])
print(s, s2)
print('\n----------------------\n')

"""
    def add(self, *args, **kwargs)
    向集合中添加数据
"""
print('向集合中添加数据: add()')
s = {1, 'b', ('cc', 4,)}
s.add('hello')
print(s)
print('\n----------------------\n')

"""
    def update(self, *args, **kwargs)
    更新集合,可添加多个值--->必须传入可迭代对象
"""
print(' 更新集合,可添加多个值: update()')
s1 = {'aa', 11, 'bb', 22}
s2 = {'cc', 'dd'}
s1.update(s2)
s1.update('ee', 'ff')
print(s1)
print('\n----------------------\n')

"""
    def clear(self, *args, **kwargs)
    清空集合中的数据
"""
print('清空集合中的数据: clear()')
s = {1, 'b', ('cc', 4,)}
s.clear()
print(s)
print('\n----------------------\n')

"""
    def copy(self, *args, **kwargs)
    集合复制
"""
print("集合复制: copy()")
s = {1, 'b', ('cc', 4,)}
s_copy = s.copy()
print(s_copy)
print('\n----------------------\n')

"""
    def pop(self, *args, **kwargs)
    随机移除一个元素并返回该元素
"""
print("随机弹出一个元素并返回该元素: pop()")
s = {1, 'b', ('cc', 4,)}
s_pop = s.pop()
print(s, s_pop)
print('\n----------------------\n')

"""
    def remove(self, *args, **kwargs)
    移除指定元素--->不存在会报错
"""
print('移除指定元素: remove()')
s = {1, 'b', ('cc', 4,)}
s.remove('b')
print(s)
print('\n----------------------\n')

"""
    def discard(self, *args, **kwargs)
    移除指定元素--->不存在不报错
"""
print('移除指定元素: discard()')
s = {1, 'b', ('cc', 4,)}
s.discard(1111)
print(s)
print('\n----------------------\n')

"""
    def difference(self, *args, **kwargs)'
    求两个集合的差集
"""
print('求两个集合的差集: difference()')
s1 = {'aa', 11, 'bb', 22}
s2 = {'aa', 'bb', 'cc', 'dd'}
s_difference = s1.difference(s2)
print('差集', s_difference)
print('差集', s1 - s2)
print('\n----------------------\n')

"""
    def intersection(self, *args, **kwargs)
    求两个集合的交集
"""
print('求两个集合的交集: intersection()')
s1 = {'aa', 11, 'bb', 22}
s2 = {'aa', 'bb', 'cc', 'dd'}
s_intersection = s1.intersection(s2)
print('交集', s_intersection)
print('交集', s1 & s2)
print('\n----------------------\n')

"""
    def union(self, *args, **kwargs)
    求两个集合的并集
"""
print('求两个集合的并集: union()')
s1 = {'aa', 11, 'bb', 22}
s2 = {'aa', 'bb', 'cc', 'dd'}
print("")
s_union = s1.union(s2)
print('并集', s_union)
print('并集', s1 | s2)
print('\n----------------------\n')

"""
    def symmetric_difference(self, *args, **kwargs)
    求两个集合的交叉补集
"""
print('求两个集合的交叉补集:')
s1 = {'aa', 11, 'bb', 22}
s2 = {'aa', 'bb', 'cc', 'dd'}
s_symmetric_difference = s1.symmetric_difference(s2)
print('交叉补集', s_symmetric_difference)
print('交叉补集', s1 ^ s2)
print('\n----------------------\n')

"""
    def difference_update(self, *args, **kwargs)
    求集合a和集合b的差集并将结果赋值给a
"""
print('求集合a和集合b的差集并将结果赋值给a: difference_update()')
s1 = {'aa', 11, 'bb', 22}
s2 = {'aa', 'bb', 'cc', 'dd'}
s1.difference_update(s2)
# s1 = s1 - s2
print(s1)
print('\n----------------------\n')

"""
    def intersection_update(self, *args, **kwargs)
    求集合a和集合b的交集并将结果赋值给a
"""
print('求两个集合的交集: intersection_update()')
s1 = {'aa', 11, 'bb', 22}
s2 = {'aa', 'bb', 'cc', 'dd'}
s1.intersection_update(s2)
# s1 = s1 & s2
print(s1)
print('\n----------------------\n')

"""
    def symmetric_difference_update(self, *args, **kwargs)
    求集合a和集合b的交叉补集并将结果赋值给a
"""
s1 = {'aa', 11, 'bb', 22}
s2 = {'aa', 'bb', 'cc', 'dd'}
s1.symmetric_difference_update(s2)
print(s1)

"""
    def isdisjoint(self, *args, **kwargs)
    判断两个集合是否有交集---交集为空时返回True
"""
print('判断两个集合是否有交集: isdisjoint()')
s1 = {11, 22}
s2 = {33, 44}
print(s1.isdisjoint(s2))
print('\n----------------------\n')

"""
    def issubset(self, *args, **kwargs)
    判断一个集合是否为某个集合的子集
"""
print('判断一个集合是否为某个集合的子集: issubset()')
s1 = {11, 22}
s2 = {11, 22, 33, 44}
print(s1.issubset(s2))
print('\n----------------------\n')

"""
    def issuperset(self, *args, **kwargs)
    判断一个集合是否为某个集合的父集
"""
print('判断一个集合是否为某个集合的父集: issuperset()')
s1 = {11, 22}
s2 = {11, 22, 33, 44}
print(s2.issuperset(s1))
print('\n----------------------\n')
