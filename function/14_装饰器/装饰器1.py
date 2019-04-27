#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 装饰器
    @Author: changchun_wu
    @Date: 2019/4/23 21:14
    @Version: 1.0 
"""

### 装饰器其实就是一个函数
### 装饰器的使用规则:
    # 1. 不修改被装饰对象的源代码
    # 2. 不修改被装饰对象的调用方式
# 装饰器 = 高阶函数(函数的参数是一个函数/函数的返回值是一个函数) + 嵌套 + 闭包

# 高阶函数---返回值是一个函数
import time

name = 'alex'
def outer():
    name = 'allen'
    def inner():
        time.sleep(2)
        print('内层函数',name)
    print('外层函数')
    return inner
inner = outer()
inner()     # 可以不该表函数的调用方式

# 高阶函数---参数是函数名
name = 'allen'
def tt(func):
    name = 'johnson'
    print(name)
    start_time = time.time()
    time.sleep(2)
    func()
    stop_time = time.time()     # 可以添加代码
    print('运行时间: %s'%(stop_time-start_time))

def nn():
    print(name)

# tt(nn)      # 会该表函数的调用方式

# 使用装饰器--无返回值和参数
def timer1(func):
    def wrapper():
        start_time = time.time()
        time.sleep(1)
        func()
        stop_time = time.time()
        print('运行时间: %s'%(stop_time-start_time))
    return wrapper

def test():
    print('test')

test = timer1(test)
test()
print('------------------\n')

# 使用装饰器--有返回值无参数
def timer2(func):
    def wrapper():
        start_time = time.time()
        time.sleep(1)
        res = func()
        stop_time = time.time()
        print('运行时间: %s' % (stop_time - start_time))
        return res
    return wrapper

def test():
    print('test')
    return '你好'

test = timer2(test)
result = test()  # 相当于执行wrapper()函数,但是wrapper函数并没有返回值,故需要接收wrapper函数中调用函数的返回值
print(result)
print('------------------\n')

# 使用装饰器--有参数有返回值
def timer(func):
    def wrapper(name):
        start_time = time.time()
        time.sleep(1)
        res = func(name)
        stop_time = time.time()
        print('运行时间: %s' % (stop_time - start_time))
        return res
    return wrapper

def test(name):
    print(name)
    return name

test = timer(test)
result = test('alex')
print(result)

# 使用装饰器--终极代码
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        time.sleep(1)
        res = func(*args,**kwargs)
        stop_time = time.time()
        print('运行时间: %s' % (stop_time - start_time))
        return res
    return wrapper

@timer  # 这里的@timer相当于 test = timer(test)
def test(name):
    print(name)
    return name

result = test('alex')
print(result)
