#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 列表
    @Author: changchun_wu
    @Date: 2019/3/27 15:27
    @Version: 1.0 
"""
####列表是有序的, 元素可以被修改

"""
    def append(self, *args, **kwargs)
    向列表中追加元素
"""
li = ['aa', 11, 'bb', 22, False]
print('向列表中追加元素: append()')
li.append('append')
print(li)
print('\n-------------------------\n')

"""
    def clear(self, *args, **kwargs)
    清空列表中的元素
"""
print('清空列表中的元素: clear()')
li = ['aa', 11, 'bb', 22, False]
li.clear()
print(li)
print('\n-------------------------\n')

"""
    def copy(self, *args, **kwargs)
    数组的拷贝
"""
print('数组的拷贝: copy()')
li = ['aa', 11, 'bb', 22, False]
new_li = li.copy()
print(new_li)
print('\n-------------------------\n')

"""
    def count(self, *args, **kwargs)
    统计列表中某个元素的个数
"""
print('统计列表中某个元素的个数: count()')
li = ['aa', 11, 11, 'bb', 22, False]
count_li = li.count(11)
print(count_li)
print('\n-------------------------\n')

"""
    def extend(self, *args, **kwargs)
    扩展列表, 只支持可迭代的对象--list/str
"""
print('扩展列表, 只支持可迭代的数据类型: extend()')
li = ['aa', 11, 11, 'bb', 22, False]
li.extend('ex')
print(li)
li.extend(['extend', 'ex'])
print(li)
print('\n-------------------------\n')

"""
    def index(self, *args, **kwargs)
    获取列表中某个元素的索引
        不带参数,从左往右找,只查询第一个该元素
    args1: 要查询的元素
    args2: 起始索引位置
    args3: 结束索引位置
"""
print('获取列表中某个元素的索引--只查询第一个该元素: index()')
li = ['aa', 11, 'bb', 11, 22, False]
li_index = li.index(11, 2, 4)
print(li_index)
print('\n-------------------------\n')

"""
    def insert(self, *args, **kwargs)
    向指定索引插入元素
"""
print('向指定索引插入元素: insert()')
li = ['aa', 11, 'bb', 11, 22, False]
li.insert(2, 'insert')
print(li)
print('\n-------------------------\n')

"""
    def pop(self, *args, **kwargs)
    默认移除最右边的元素
    添加参数: 弹出(移除)指定索引位置的元素
"""
print('移除指定索引位置的元素: pop()')
li = ['aa', 11, 'bb', 11, 22, False]
li.pop(1)
print(li)
print('\n-------------------------\n')

"""
    def remove(self, *args, **kwargs)
    移除指定的元素--默认从左到右查询到第一个 
"""
print('')
li = ['aa', 11, 'bb', 11, 22, False]
li.remove(11)
print(li)
print('\n-------------------------\n')
# pop()/remove()/del三种方式删除

"""
    def reverse(self, *args, **kwargs)
    列表元素反转
"""
print('列表元素反转: reverse()')
li = ['aa', 11, 'bb', 11, 22, False]
li.reverse()
print(li)
print('\n-------------------------\n')

"""
    def sort(self, *args, **kwargs)
    对无序列表进行排序
"""
print('对无序列表进行排序: sort()')
li = [11, 33, 22, 44]
li.sort(reverse=True)
print(li)
print('\n-------------------------\n')
