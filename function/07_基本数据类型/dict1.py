#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Description: 
    @ClassName: dict1
    @Author: changchun_wu
    @Date: 2019/3/27 19:49
    @Version: 1.0 
"""

print('字典的使用')

info = {
    2: 222,
    'admin': '张三三',
    ('aa', 22): ['bb', ('cc', 22,)],
    'dd': True,
    True: '111'
}
print(info)
print('\n----------------------\n')

# 通过key找到指定元素的value
print('通过key找到value的值')
info = {
    'k1': 222,
    'k2': '张三三',
    'k3': ['bb', ('cc', 22,)],
    'k4': True,
    'k5': [999, 'mmm', {'k1': 11, 'k2': (66, 'oo'), 'k3': 33, 'k4': 44}]
}
v1 = info['k2']
print(v1)
v2 = info['k5'][2]['k2'][0]
print(v2)
print('\n----------------------\n')

# 删除key
print('删除指定的key: del')
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
del info['k2']
print(info)
print('\n----------------------\n')

# for循环
info = {'k1': 11, 'k2': 22, 'k3': 33, 'k4': 44}
print('获取所有的key: keys()')
for keys in info.keys():
    print(keys)
print('\n----------------------\n')

print('获取所有的value: values()')
for values in info.values():
    print(values)
print('\n----------------------\n')

print('获取所有的key和value: items()')
for keys, values in info.items():
    print(keys, values)
print('\n----------------------\n')
