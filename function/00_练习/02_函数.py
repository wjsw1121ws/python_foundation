#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 02_函数
    @Author: changchun_wu
    @Date: 2019/4/17 22:03
    @Version: 1.0 
"""

# 函数参数的使用
from functools import reduce


def func(*args,**kwargs):
    print(args,kwargs)

func(*[1,2],{'name':'alex'})       # (1, 2, {'name': 'alex'}) {}
func(*[1,2],**{'name':'alex'})     # (1, 2) {'name': 'alex'}
print('------------------------\n')

# 函数返回值的使用
def func1(x=1,*y,**z):
    print(x,y,z)    # 1:  1,(),{'name':alex}
    return y        # 2:  ()
    print(x)        # 遇到return函数就不运行了,该段代码不会执行
def func2(arg):
    ret = func1(name=arg)
    print(ret)      # 3: None
result = func2('funk')
print(result)
print('------------------------\n')

def f1(arg):
    print(arg+100)      # 108
def f2(arg):
    ret = f1(arg+1)     # None
    print(arg)          # 7
    print(ret)          # None

ret = f2(7)
print(ret)              # None
print('------------------------\n')

s = '老男孩'.encode('utf-8')
print(s)
print(bytes('老男孩','utf-8'))
print(s.decode('utf-8'))
print('------------------------\n')

# zip()和join()的使用
# 利用字符串实现功能
# l1 = ['alex',22,33,44,55] l2 = ['is',22,33,44,55]
# l3 = ['good',22,33,44,55] l4 = ['guy',22,33,44,55]
# 获取字符串s = 'alex_is_good_gay'
l1 = ['alex',22,33,44,55]
l2 = ['is',22,33,44,55]
l3 = ['good',22,33,44,55]
l4 = ['guy',22,33,44,55]
print('_'.join(list(zip(l1,l2,l3,l4))[0]))
print('------------------------\n')

# 局部变量和全局变量
NAME = ['alex','allen']
def func1():
    NAME = 'johnson'
    print(NAME)
func1()
print(NAME)
print('------------------------\n')

# global关键字的使用
def func2():
    global NAME
    NAME = 'johnson'
    print(NAME)
func2()
print(NAME)
print('------------------------\n')

# 全局变量
NAME = ['alex','allen']
def func3():
    NAME.append('johnson')
    print(NAME)
func3()
print(NAME)
print('------------------------\n')

NAME = ['alex','allen']
# def func4():
#     NAME = 123
#     global NAME
#     print(NAME)
# func4()
# print(NAME)       # 运行出错

name = 'root'
def func1():
    name = 'steven'
    def outer():
        name = 'eric'
        def inner():
            global name
            name = '懵逼了吧'
        print(name)
    print(name)
ret = func1()
print(ret)      # steven  None
print(name)     # root
print('------------------------\n')

name = 'root'
def func2():
    name = 'steven'
    def outer():
        name = 'eric'
        def inner():
            global name
            name = '懵逼了吧'
        print(name)
    o = outer()
    print(o)
    print(name)
ret = func2()
print(ret)
            # eric
            # None
            # steven
            # None
print(name)     # root
print('------------------------\n')

name = 'root'
def func3():
    name = 'steven'
    def outer():
        name = 'eric'
        def inner():
            global name
            name = '懵逼了吧'
        inner()
        print(name)
    o = outer()
    print(o)
    print(name)
ret = func3()
print(ret)
            # eric
            # None
            # seven
            # None
print(name)    # 懵逼了吧
print('------------------------\n')

name = 'root'
def func4():
    name = 'steven'
    def outer():
        name = 'eric'
        def inner():
            nonlocal name
            name = '懵逼了吧'
        inner()
        print(name)
    o = outer()
    print(o)
    print(name)
ret = func4()
print(ret)
            # 懵逼了吧
            # None
            # seven
            # None
print(name)    # root
print('------------------------\n')

name = 'alex'
def outer(func):
    name = 'allen'
    func()
def show():
    print(name)
outer(show)     # alex
print('------------------------\n')

name = 'alex'
def outer():
    name = 'allen'
    def inner():
        print(name)
    return inner

ret = outer()
ret()           # allen
# print(ret)
res = ret()     # allen
print(res)      # None
print('------------------------\n')

# 递归实现1*2*3...*7
def func1(x):
    # while x ==1:
    if x ==1:
        return 1
    return x*func1(x-1)
print(func1(7))
print('------------------------\n')

def func2(x,y=1):
    for i in range(1,x+1):
        y*=i
    return y
print(func2(7))
print('------------------------\n')

# print(reduce(lambda x,y:x*y,list(range(1,8))))
print(reduce(lambda x,y:x*y,[i for i in range(1,8)]))
print('------------------------\n')

# 猴子吃桃的故事
def eat():
    s = 1
    for i in range(1,10):
        s= (s+1)*2
    return s
print(eat())

s = 1
func = lambda x:(x+1)*2
for i in range(1,10):
    s = func(s)
print(s)