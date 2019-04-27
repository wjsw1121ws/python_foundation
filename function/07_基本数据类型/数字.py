#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  * @Description:
  * @ClassName: 数字
  * @Author: changchun_wu
  * @Date: 2019/3/25 16:24
  * @Version: 1.0 
""" 
m = '100'   # int

print('字符串与数字之间的转换: 默认是十进制 ')
print(type(m), m)
n = int(m) + 20
print(type(n), n)
print('-------------------------')

print('字符串与数字之间的转换: 指定进制之间的转换 ')
a = 'a'
b = int(a, base=16)
print(b)
print('-------------------------')

print('求数字的二进制的最小位数: bit_length()')
m = 4
n = m.bit_length()
print(n)
print('-------------------------')
