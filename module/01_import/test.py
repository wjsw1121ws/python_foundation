#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: test
    @Author: changchun_wu
    @Date: 2019/4/24 21:53
    @Version: 1.0 
"""

# import cal

### import
# 会先执行调用的文件
# 引入变量名

# print(cal.add(3,6))
# print(cal.sub(3,6))
# print('-------------------\n')

# from cal import add
# from cal import sub
# from cal import *   # 不推荐

# from cal import add,sub
# print(add(3,5))
# print(sub(3,5))
# print('-------------------\n')

from my_module import cal
print(cal.add(1,2))
print(cal.sub(1,2))
print('-------------------\n')
