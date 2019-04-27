#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  * @Description: 
  * @ClassName: dict
  * @Author: changchun_wu
  * @Date: 2019/3/25 16:30
  * @Version: 1.0 
"""
dict

#### 字典是无序的
#### 字典由键值对组成
#### 字典的key不能是列表
#### key值不能重复
#### 字典的value可以是任意类型

print('***********普通方法*************')
"""
    def clear(self)
    清空字典中的键值对
"""
print('清空字典中的键值对: clear()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info.clear()
print(info)
print('\n----------------------\n')

"""
    def copy(self)
    字典的拷贝
"""
print('字典的拷贝: copy()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info_copy = info.copy()
print(info_copy)
print('\n----------------------\n')

print('***********静态方法*************')
"""
    def fromkeys(*args, **kwargs)
    根据序列创建字典并指定统一的值
"""
print('根据序列创建字典并指定统一的值: fromkeys()')
dict_fromkeys = dict.fromkeys(['k1', 'k2', 'k3'], 'kkk')
print(dict_fromkeys)
print('\n----------------------\n')

"""
    def get(self, *args, **kwargs)
    根据字典的key获取字典的value
    args1: 传入的key--如果没有设置args2且key不存在,则返回默认值(None)
    args2: key不存在时返回的数据
"""
print('根据字典的key获取字典的value: get()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info_get = info.get('k2', 222)
print(info_get)
print('\n----------------------\n')

"""
    def items(self): # real signature unknown
    获取字典中所有的key和value
"""
print('获取字典中所有的key和value: items()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info_items = info.items()
print(info_items)
print('\n----------------------\n')

"""
    def keys(self)
    获取字典中所有的key
"""
print('获取字典中所有的key: keys()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info_keys = info.keys()
print(info_keys)
print('\n----------------------\n')

"""
    def values(self)
    获取字典中所有的value
"""
print('获取字典中所有的value: values()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info_values = info.values()
print(info_values)
print('\n----------------------\n')

"""
    def pop(self, k, d=None)
    移除指定字典中的key
    args1: 要移除的key---如果不设定args2,那么如果key不存在返回None
    args2: key不存在时的返回值
"""
print('移除指定字典中的key: pop()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info_pop = info.pop('k22', '不存在')
print(info, info_pop)
print('\n----------------------\n')

"""
    def popitem(self)
    随机从字典中删除一组键值对(3.6之后默认dict是有序的,则是弹出最有一个)
"""
print('随机从字典中删除一组键值对: popitem()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info_popitem = info.popitem()
print(info, info_popitem)
print('\n----------------------\n')

"""
    def setdefault(self, *args, **kwargs)
    key存在: 不设置值并返回key对应的value
    key不存在: 向字典中添加一组键值对并返回新设置key对应的value
"""
print('设置值: info_setdefault()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
info_setdefault = info.setdefault('k1', 222)
print(info, info_setdefault)
print('\n----------------------\n')

"""
    def update(self, E=None, **F)
    更新字典--两种方式
    key存在: 不做修改返回已存在的值
    key不存在: 将key和value添加到字典中
"""
print('更新字典: update()')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
# info.update(k1=11111, k6=66)
info.update({'k1': 11111, 'k6': 66})
print(info)
print('\n----------------------\n')
