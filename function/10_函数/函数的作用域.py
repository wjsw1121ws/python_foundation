#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 函数的作用域
    @Author: changchun_wu
    @Date: 2019/4/3 23:41
    @Version: 1.0 
"""

#############函数的作用域
# 函数的执行顺序时从外到里, 不能直接跳过外层函数执行嵌套的函数
# 内层函数不能跳过外层函数直接调用, 必须在外层函数中一层一层调用

name = 'hh'


def aa():
    def bb():
        name = 'bb'
        def cc():
            print(name)
        return cc
    return bb
# bb = aa()
# cc = bb()
# rees = cc()
print(aa()()())
