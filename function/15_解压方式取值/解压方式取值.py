#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 解压方式取值
    @Author: changchun_wu
    @Date: 2019/4/23 23:51
    @Version: 1.0 
"""

# 一一对应取元素的值
a,b,c =[1,2,3]
print(a,b,c)

# 取元素的开头和结尾
li = [1,2,3,4,5,6,7,8,9]
a,*_,c = li
print(a,_,c)
a,*b,c = li
print(a,b,c)
*a,b = li
print(a,b)

# 交换a和b的值
a= 1
b = 2
a,b = b,a
print(a,b)
