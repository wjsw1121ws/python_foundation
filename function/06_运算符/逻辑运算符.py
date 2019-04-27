#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 逻辑运算符
    @Author: changchun_wu
    @Date: 2019/3/24 21:49
    @Version: 1.0 
"""

"""
    补充: 
        先计算括号内
        (name == 'admin0' or nickname == 'sansan')  and password == '123456' 
                        True                                    True      --->True
    执行顺序:
        从前到后
        True or     --->True
        True and    --->继续执行
        False or    --->继续执行
        False and   --->False
        
        name = 'admin'
        password = '123456'
        nickname = 'sansan'
        name == 'admin' and password == '123456' or nickname == 'san'
            True    --->继续执行    True        --->不再执行                --->True
        name == 'admin0' and password == '123456' or nickname == 'san'
            False   --->不再执行                                           --->False  
        name == 'admin0' or nickname == 'sansan'  and password == '123456' 
            False   --->继续执行     True       --->继续执行     True        --->True
"""


m = 2
n = 3

print('与')
if m == 2 and n == 2:
    print('true')
else:
    print('false')

print('或')
if m == 2 or n == 2:
    print(True)
else:
    print(False)

print('非')
if not m == 2:
    print(True)
else:
    print(False)
