#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 成员运算
    @Author: changchun_wu
    @Date: 2019/3/24 21:55
    @Version: 1.0 
"""

m = '情深深雨蒙蒙'

print('in')    # 子序列
if '情深深' in m:
    print(True)
else:
    print(False)


print('not in')
if '情蒙蒙' not in m:
    print(True)
else:
    print(False)
