#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 函数
    @Author: changchun_wu
    @Date: 2019/4/17 10:34
    @Version: 1.0 
"""

# 根据范围取其中能整除3和7的所有数的和,已经符合条件的个数
# 通过for循环实现
from functools import reduce


def test1(m, n):
    num = 0
    sum = 0
    for i in range(m, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            num += 1
            sum += i
            i += 1
        if i == n:
            return num, sum


# print(test1(1, 44))

######## 通过递归实现
def test2(m, n, num=0, sum=0):
    while True:
        if m == n:
            return num, sum
        if m % 3 == 0 and m % 7 == 0:
            num += 1
            sum += m
        return test2(m + 1, n, num, sum)


print(test2(1, 44))


# 函数在传递参数时是引用还是复制值
def func(x):
    print(id(x))


func('a')
func('b')

# 三元运算符的使用
# 创建一个列表[1,2,....10]
li = [i for i in range(1, 11)]
print(li)
# 奇数偶数判断
flag = ['偶数' if 9 % 2 == 0 else '奇数']
print(flag)

# lambda表达式的使用
# map,对列表元素中的每个元素进行操作
li = ['alex', 'allen', 'johnson']
print(list(map(lambda x: x + '_sb', li)))
# filter,对列表中的元素进行过滤
print(list(filter(lambda x: x.endswith('n'), li)))
# reduce,将列表中的元素进行统计
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x, y: x + y, li))

# 获取两个列表中相同的元素, [11,22,33],[22,33,44]
# set集合操作
l1 = [11,22,33]
l2 = [22,33,44]
print(set(l1) & set(l2))
print(set(l1) | set(l2))
print(set(l1)  ^ set(l2) )
print(set(l1) - set(l2))

# 定义函数统计一个字符串中大写字母,小写字母,数字的个数
# zip的使用
st = 'AvvS12eew'
def tt(st,a=0,b=0,c=0):
    for i in st:
        if i.isupper():
            a+=1
        if i.islower():
            b+=1
        if i.isdigit():
            c+=1
    return dict(zip(('k1','k2','k3'),(a,b,c)))
print(tt(st))

# 参数类型的使用
def test(x,y,*args):
    print(x,y,args)

test(1,2,3,4,5,6)

def test(x,*args,**kwargs):
    print(x,args,kwargs)

test(1,2,3,4,5,6)