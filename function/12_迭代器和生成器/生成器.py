#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 生成器
    @Author: changchun_wu
    @Date: 2019/4/14 17:49
    @Version: 1.0 
"""


# 生成器的函数表现显示
# 生成器就是可迭代对象
# 使用yield关键字得到生成器---yield实现了迭代器协议
# yield相当于return的使用, 但是yield可以返回多个
# def test():
#     yield 1
#     yield 2
#     yield 3
#
#
# tt = test()
# print(tt)
# print(tt.__next__())
# print(tt.__next__())
# print(tt.__next__())

# 模拟包子铺
def product_baozi():
    for i in range(100):
        print('生产包子')
        yield '一叠包子%s'%i
        print('卖包子')

eat_baozi = product_baozi()
eat_baozi.__next__()
eat_baozi.__next__()
# for i in eat_baozi:
#     print(i)

# 生成器表达式
li = ('鸡蛋%s' % i for i in range(10))
print(li)
print(li.__next__())
print(li.__next__())

li = ('鸡蛋%s' % i for i in range(10) if i > 2 and i < 7)
print(li)
print(li.__next__())

# sum()也是实现了迭代器协议的生成器对象
print(sum(i for i in range(10)))