#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: format格式化
    @Author: changchun_wu
    @Date: 2019/4/1 19:56
    @Version: 1.0 
"""

print('一一对应关系方式的格式化')
"""
    一一对应关系方式的格式化
"""
msg = 'my name is {} and my age is {} and my hobby is {}'
msg_format = msg.format('alex', 20, 'swimming')
print(msg_format)
print('\n------------------------\n')

print('占位符方式的格式化')
"""
    占位符方式的格式化
"""
msg = 'my name is {0} and my age is {2} and my hobby is {1}'
msg_format = msg.format('allen', 'basketball', 30)
print(msg_format)
############
info = 'my age is {1} and her age is {1}'
info_format = info.format('allen', 18, 'sss')
print(info_format)
print('\n------------------------\n')

print('使用键的形式格式化')
"""
    使用键的形式格式化
"""
msg = 'my name is {name} and my age is {age} and my hobby is {hobby}'
msg_format = msg.format(name='johnson', age='55', hobby='dance')
print(msg_format)
############
msg_format2 = msg.format(**{'name': 'johnson', 'age': 22, 'hobby': 'baseball'})
print(msg_format2)
msg_format_map = msg.format_map({'name': 'johnson', 'age': 55, 'hobby': 'sing'})
print(msg_format_map)
print('\n------------------------\n')

print('使用索引的方式')
"""
    使用索引的方式
"""
msg = 'allen is {0[0]},alex is {0[1]} and alic is {0[2]}'
msg_format = msg.format([1, 2, 3], [4, 5, 6])
print(msg_format)
print('\n------------------------\n')

print('根据参数类型格式化')
msg = 'my name is {:s}, my age is {:d} and my grade is {:.2f}'
msg_format = msg.format('alex', 22, 88.88888)
print(msg_format)
############
msg_format2 = msg.format(*['allen', 25, 90.666])
print(msg_format2)
print('\n------------------------\n')

print('根据参数类型格式化2')
msg = 'my name is {name:s}, my age is {age:d} and my grade is {grade:.2f}'
msg_format = msg.format(name='ali', age=25, grade=90.8888)
print(msg_format)
############
msg_format2 = msg.format(**({'name': 'bob', 'age': 8, 'grade': 59.4444}))
print(msg_format2)
print('\n------------------------\n')

print('占位符的其他用法')
msg = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}"
msg_format = msg.format(15, 15, 15, 15, 15, 15.87623, 2)
print(msg_format)

msg = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}"
msg_format = msg.format(15)
print(msg_format)
msg = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}"
msg_format = msg.format(num=15)
print(msg_format)
