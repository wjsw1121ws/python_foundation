#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 模拟吃包子
    @ClassName: 生产者消费者
    @Author: changchun_wu
    @Date: 2019/4/16 7:36
    @Version: 1.0 
"""


# 定义生产包子的类
def producer(x):
    print('生产了包子中: 第%s个包子' % x)
    yield x
    # send接收yield的返回值
    # xx.send(x)


def consumer(func):
    for i in range(100):
        xx = func(i)
        xx.__next__()
        print('吃包子: 第%s个'%i)


consumer(producer)

def test_send():
    xx = yield 1
    print('第一次',xx)
    yy = yield
    print('第二次', yy)
    zz = yield
    print('第三次', zz)


tt = test_send()
aa = tt.__next__()
tt.send('你好')
tt.send('hello')
tt.send('hi')
