#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 内置函数
    @Author: changchun_wu
    @Date: 2019/4/8 16:45
    @Version: 1.0 
"""

print('abs()')
print(abs(-3))
print('--------------------\n')

print('all()------列表中的每个元素都是True则返回True, 如果列表是空则返回True')
print(all(['alex', 0]))
print(all([]))
print('--------------------\n')

print('any()-------列表中的任意一个元素为True,则返回True')
print(any(['aaa', 0]))
print('--------------------\n')

print('bin()-----将十进制转为二进制')
print(bin(10))
print('--------------------\n')

print('oct()-----将十进制转为八进制')
print(oct(10))
print('--------------------\n')

print('hex()-----将十进制转十六进制')
print(hex(10))
print('--------------------\n')

print('bool()-----除了0, {}, [], '', None, (),其他都是True')
### 0   {}  [] ''   None    ()
print(bool(''))
print('--------------------\n')

print('bytes()-----将字符串进行编码并返回其二进制数')
print(bytes('你好', encoding='utf-8'))
print(bytes('你好', encoding='utf-8').decode('gbk'))
# ASCII码不能编码中文
# print(bytes('你好',encoding='utf-8').decode('ascii'))
print('--------------------\n')

print('chr()-----对数字进行ascii码打印')
print(chr(46))
print('--------------------\n')

print('dict()-----创建一个字典')
print(dict(name='alex', age=28))
print(dict({'name': 'alex', 'age': 28}))
print('--------------------\n')

print('dir()-----查看每个数据类型有哪些方法')
print(dir(dict))
print('--------------------\n')

print('divmod()------将两个元素的商和余数放入元组中输出')
print(divmod(10, 3))
print('--------------------\n')

print('eval()')
print('功能一----将字符串中的元组/字典/列表提取出来')
dic_str = "{'k1'='aa','k2'='bb'}"
list_str = "['aa','bb']"
print(eval(list_str))
print('功能二-----将字符串中的数学计算提取出来并计算')
express = '1+2*3/2+5'
print(eval(express))
print('--------------------\n')

### 不可变类型才能进行hash操作
print('hash()----获取不可变类型的hash值')
print(hash('aaa'))
print(hash('bbb'))
print('--------------------\n')

print('help()------获取某个内置方法的帮助文档')
print(help(all))
print('--------------------\n')

print('id()------打印一个对象的内存地址')
print(id('bbb'))
print('--------------------\n')

print('isinstance()-----判断某个对象是否是某种数据类型')
print(isinstance('aaa', str))
print('--------------------\n')

print('globals()------打印类中的所有全局变量')
NAME = '哈哈哈哈哈'
print(globals())
print('--------------------\n')

print(' ()------打印类中的所有局部变量')


def test():
    name = '哈哈哈哈'
    print(locals())


test()
print('--------------------\n')

print('zip()')
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))
print(list(zip(['a', 'b', 'c'], [1, 2, 3, 4])))
print(list(zip(['a', 'b', 'c', 'd'], [1, 2, 3])))
dic = {'k1': 'alex', 'k2': 3, 'k3': (1, 2)}
print(list(zip(dic.keys(), dic.values())))
print('--------------------\n')

print('取对象中的最小和最大值----比较列表')
li = [1, 2, 100, -1]
print(max(li))
print(min(li))
print('--------------------')

print('取对象中的最小和最大值----比较字典')
dic = {'k1': 1, 'k2': 30, 'k3': 100}
print((max((zip(dic.values(), dic.keys())))))
print('--------------------')

print('取对象中的最小和最大值----比较复杂列表')
li = [(1, 'a'), (3, 'b'), (2, 'c')]
print((max(li)))
print('--------------------')

# li = ['a10','b12','c11',100]  ########不同数据类型中间不能比较
li = ['a10', 'b12', 'c11']  ########相同数据类型从左到右依次比较
print(max(li))
print('--------------------')

people = [
    {'name': 'alex', 'age': 10},
    {'name': 'allen', 'age': 18},
    {'name': 'john', 'age': 8},
    {'name': 'wcc', 'age': 20}
]

# li = []
# def people_test():
#     for item in people:
#         li.append(item['age'])
#     return li
#
# print(people_test())

print(max(people, key=lambda x: x['age']))
print('--------------------\n')

print('chr()/ord()------数字和unicode码之间的转换')
print(chr(97))
print(ord('a'))
print('--------------------\n')

print('pow()----两个参数相当于取平方,三个参数则是取平方的余数')
print(pow(2, 3))  # 2**3
print(pow(3, 3, 5))  # 3**3%2
print('--------------------\n')

print('reversed()----列表反转')
li = [1, 2, 3, 4]
print(list(reversed(li)))
print('--------------------\n')

print('round()----四舍五入(取整)')
print(round(3.55555))
print('--------------------\n')

print('slice()-----切片')
st = 'hello'
print(st[slice(3, 5)])
s = 'helloworld'
print(s[slice(1, 7, 2)])
ss = slice(1, 7, 2)
print(ss.start, ss.stop, ss.step)
print('--------------------\n')

print('sorted()------排序')
li = [1, 5, 2, 7]
li = [1, 5, 2, 7, 'a']  # 排序就是按照从小大小的顺序比较,不同类型之间比较会报错
# print(sorted(li))
print('--------------------')

people = [
    {'name': 'alex', 'age': 10},
    {'name': 'allen', 'age': 18},
    {'name': 'john', 'age': 8},
    {'name': 'wcc', 'age': 20}
]

# print(sorted(people, key=lambda x: x['age']))

dic = {
    'alex': 200,
    'john': 250,
    'bob': 100
}
print(sorted(dic, key=lambda key: dic[key]))
print(sorted(zip(dic.values(), dic.keys())))
print('--------------------\n')

print('str()')
print(str({'a': 1}), type(str({'a': 1})))
tt = eval(str({'a': 1}))
print(tt,type(tt))
print('--------------------\n')

print('sum()---求和')
li = [2,4,6]
print(sum(li))

print('vars()----没有参数相当于locals()的用法,有参数则将类中的所有属性显示成字典的形式')
def vars_test():
    name = 'alex'
    print(locals())
    print(vars())
vars_test()
print(vars(int))
print('--------------------\n')
