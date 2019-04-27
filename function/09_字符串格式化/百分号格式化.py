#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 使用%进行字符串的格式化
    @ClassName: str_format
    @Author: changchun_wu
    @Date: 2019/4/1 11:41
    @Version: 1.0 
"""
print('打印字符串%s')
'''
    打印字符串%s
'''
# 字符串
msg = 'my name is %s and my age is 20'%'alex'
print(msg)

# 多个字符串
msg = 'my name is %s and my hobby is %s'%('alex','swim')
print(msg)

# 列表元组
msg = 'my hobby is %s, and her hobby is %s'%(['swim','basketball'],('dance','sang',))
print(msg)

# 取固定长度字符串
msg = '%.5s'%'ABCDEFGHIJK'
print(msg)
print('\n---------------------\n')

print('打印数字%d')
""""
    打印数字%d
"""
msg = 'today is my %d birthday'%20
age = 30
info = 'my friend is %d years old'%age
print(msg)
print(info)
print('\n---------------------\n')

print('打印浮点数%f')
"""
    打印浮点数%f
"""
msg = '%f'%2.555555555555       # 默认保留6位
print(msg)
info = '%.2f'%2.5555555         # 设置精度
print(info)
print('\n---------------------\n')

print('打印%')
"""
    打印%
"""
msg = '%.3f%%'%82.66666
print(msg)
print('\n---------------------\n')

print('使用键的形式拼接字符串')
"""
    使用键的形式拼接字符串
"""
msg = '%(name)s, %(age)d'%{'name':'alex','age':20}
print(msg)
info = '%(pp).2f'%{'pp':22.5555}
print(info)
print('\n---------------------\n')