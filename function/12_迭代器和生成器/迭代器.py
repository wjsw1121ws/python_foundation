#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 迭代器
    @Author: changchun_wu
    @Date: 2019/4/14 17:54
    @Version: 1.0 
"""

li = ['alex', 123, False]
# 调用__iter__()/iter()方法生成迭代器,变为可迭代对象
li_iter = li.__iter__()
# li_iter = iter(li)
print(li_iter)          
# 调用__next__()/next()取得迭代器中的对象
# print(next(li_iter))
print(li_iter.__next__())
print(li_iter.__next__())
print(li_iter.__next__())

