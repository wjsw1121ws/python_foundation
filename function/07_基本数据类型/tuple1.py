#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  * @Description: 
  * @ClassName: 元组
  * @Author: changchun_wu
  * @Date: 2019/3/25 16:30
  * @Version: 1.0 
"""
tuple

####元组也是可迭代对象
#### 元组的一级元素不可被修改(增删)
print('##########')
tu = ('aa', 11, 'bb', 22, False, [('cc', 33,)], ('tt', 99,))
# tu[5] = 111        #报错
#tu[5][0] = 1111
# tu[5][0][0] = 111  #报错
print(tu)
print('\n-----------------------------\n')

# 索引操作
tu = ('aa', 11, 'bb', 22, False, ['cc', 33], ('tt', 99,))
print('按索引取值')
print(tu[6])
print('\n-----------------------------\n')

# 切片操作
tu = ('aa', 11, 'bb', 22, False, ['cc', 33], ('tt', 99,))
print('取指定切片中的元素')
print(tu[1:-1])  # 开区间
print('\n-----------------------------\n')

# 取列表长度
print('取元祖长度')
tu = ('aa', 11, 'bb', 22, False, ['cc', 33], ('tt', 99,))
print(len(tu))  # 列表是按照数组的每个元素算的
print('\n-----------------------------\n')

# 判断元素是否在列表中: in
print('判断元素是否在元组中')
tu = ('aa', 11, 'bb', 22, False, ['cc', 33], ('tt', 99,))
var = 'aa' in tu
print(var)
print('\n-----------------------------\n')

# 字符串/列表与元组互转
s = 'admin'
print('字符串转元组')
t = tuple(s)
print(t)
print('\n-----------------------------\n')

print('列表转元组')
li = ['aa', 11, 'bb', 22, False, ['cc', 33], ('tt', 99,)]
print(tuple(li))
print('\n-----------------------------\n')

print('元组转列表')
tu = ('aa', 11, 'bb', 22, False, ['cc', 33], ('tt', 99,))
print(list(tu))
print('\n-----------------------------\n')

print('元组转字符串---都由字符串构成的元组')
tu = ('aa', 'cc', 'bb',)
v = "".join(tu)
print(v)
print('\n-----------------------------\n')

print('元组转字符串---由不同数据类型构成的元组')
tu = ('aa', 11, 'bb', 22, False, ['cc', 33], ('tt', 99,))
s = ''
for item in tu:
    s += str(item)
print(s)
print('\n-----------------------------\n')

# for循环
for index, item in enumerate(tu):
    print(index, item)
print('\n-----------------------------\n')
