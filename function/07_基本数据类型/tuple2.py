#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  * @Description: 
  * @ClassName: 元组
  * @Author: changchun_wu
  * @Date: 2019/3/25 16:30
  * @Version: 1.0 
"""
#### tuple---元组
#### 元组的一级元素不可被修改(增删)
#### 元组书写规范---最后面加上一个逗号 (stat1, stat2, stat3,)

tuple
"""
    def count(self, *args, **kwargs): # real signature unknown
    统计元组中某个元素出现的个数
"""
print('统计元组中某个元素出现的个数: count()')
tu = ('aa', 11, 'bb', 11, 22, False, [('cc', 33,)], ('tt', 99,))
tu_count = tu.count(11)
print(tu_count)
print('\n-----------------------------\n')

"""
    def index(self, *args, **kwargs): # real signature unknown
    统计元组中某个元素的个数
"""
print('统计元组中某个元素的个数: index()')
tu = ('aa', 11, 'bb', 11, 22, False, [('cc', 33,)], ('tt', 99,))
tu_index = tu.index(11, 2, 5)
print(tu_index)
print('\n-----------------------------\n')
