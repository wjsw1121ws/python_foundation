#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 匿名函数
    @Author: changchun_wu
    @Date: 2019/4/4 0:03
    @Version: 1.0 
"""
str

aa = lambda x:x+1
print(aa(10))

bb = lambda name:name+'_sb'
print(bb('alex'))

def xx(a,b,c):
    return a+1,b+1,c+1
print(xx(1,2,3))

cc = lambda a,b,c:(a+1,b+1,c+1)
print(cc(1,2,3))

