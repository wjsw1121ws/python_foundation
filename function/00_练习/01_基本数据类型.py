#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: test
    @Author: changchun_wu
    @Date: 2019/3/28 1:40
    @Version: 1.0 
"""

# l1和l2中不同的元素
l1 = [1, 2, 3]
l2 = [2, 3, 4]
for i in l1:
    if i not in l2:
        print(i)
for i in l2:
    if i not in l1:
        print(i)
print('--------------------------------\n')

# 1,2,3,4,5,6,7,8组成多少个互不相同且无重复数字的两位数
li = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0
for i in li:
    for j in li:
        if i != j:
            count += 1
print(count)
print('--------------------------------\n')

# 99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(i, '*', j, '=', i * j, '\t', sep='', end='')
    print()
print('--------------------------------\n')

# 输出5*5菱形
for i in range(1, 6, 2):
    print(("*" * i).center(5))
for j in reversed(range(1, 6, 2)):
    print(("*" * j).center(5))
print('--------------------------------\n')

# 5文钱可以买一只公鸡，3文钱可以买一只母鸡,1文钱可以买3只雏鸡.现在用100文钱买100只鸡，那么各有公鸡、母鸡、雏鸡多少只？
for gj in range(1, 100 // 5):
    for mj in range(1, 100 // 3 + 1):
        for cj in range(1, 100):
            if gj + mj + cj == 100 and gj * 5 + mj * 3 + cj / 3 == 100 and cj % 3 == 0:
                print(gj, mj, cj)
print('--------------------------------\n')

# 请用代码实现：利用下划线将列表的每个元素拼接成字符串，li=["alex","eric","rain"]
li = ["alex", "eric", "rain", 123]
l2 = []
for item in li:
    l2.append(str(item))
for item2 in l2:
    s = "_".join(l2)
print(s)
print('--------------------------------\n')

# tu = ("alex","eric","rain")
# 计算元组的长度
tu = ("alex", "eric", "rain")
print(len(tu))
print('--------------------------------\n')
# 获取元组中的第二个元素
print(tu[1])
print('--------------------------------\n')
# 获取元组的1-2个元素
print(tu[0:2])
print('--------------------------------\n')
# for循环输出元组中的元素
for item in tu:
    print(item, end='\t')
print()
print('--------------------------------\n')
# 利用for len range输出元组的索引
for item in range(0, len(tu)):
    print(item, tu[item], end='\t')
print()
print('--------------------------------\n')
# 利用enumerate输出元素和索引(索引从10开始)
for index, item in enumerate(tu, 10):
    print(index, item, end='\t')
print()
print('--------------------------------\n')

# tu = ('aa', 22,  {'k1': 11, 'k2': (66, 'oo'),'k3': ['alex', 44], [('cc', 33,)]}, ('tt', 99,))
tu = ('aa', 22, {'k1': 11, 'k2': (66, 'oo'), 'k3': ['alex', 44]}, [('cc', 33,)], ('tt', 99,))
# k2对应的值可以被修吗,如果可以,添加一个元素steven
print('不可以')
# k3对应的值可以被修吗,如果可以,添加一个元素steven
print('可以')
tu[2]['k3'].append('steven')
print(tu)
print('--------------------------------\n')

# nums = [2, 7, 11, 15, 1, 8]
nums = [2, 7, 11, 15, 1, 8, 7]
# 找出两个元素相加等于9的集合入[1, 8]
for index1, num1 in enumerate(nums):
    for index2, num2 in enumerate(nums):
        if num1 != num2 and num1 + num2 == 9:
            print([num1, num2], [index1, index2])
print('--------------------------------\n')

# li = ["alex", "eric", "rain"]
# 计算列表长度并输出
li = ["alex", "eric", "rain"]
print(len(li))
print('--------------------------------\n')
# 在列表中添加Steven并输出
li.append('Steven')
print(li)
print('--------------------------------\n')
# 在第一个元素后面添加Tony
li = ["alex", "eric", "rain"]
li.insert(1, 'Tony')
print(li)
print('--------------------------------\n')
# 修改第二个元素为Kelly
li = ["alex", "eric", "rain"]
li[1] = 'Kelly'
print(li)
print('--------------------------------\n')
# 删除元素eric
li = ["alex", "eric", "rain"]
li.remove('eric')
print(li)
print('--------------------------------\n')
# 删除第二个元素,并输出删除的元素
li = ["alex", "eric", "rain"]
li_pop = li.pop(1)
print(li, li_pop)
print('--------------------------------\n')
# 将列表反转
li = ["alex", "eric", "rain"]
li.reverse()
print(li)
print('--------------------------------\n')
# 输出所以的索引
li = ["alex", "eric", "rain"]
for index in range(0, len(li)):
    print(index, li[index], end='\t')
print()
for i, e in enumerate(li, 100):
    print(i, e, end='\t')
print()
print('--------------------------------\n')

# 通过for循环创建200条数据
li = ['aa', 'bb', 'cc']
for i in range(1,10):
    for item in li:

        print(item+str(i),end='\t')
    print()
print('--------------------------------\n')

user_msg = []
for i in range(1,301):
    temp = {'name':'user'+str(i),'email':'allen'+str(i)+'@163.com','password':'admin'+str(i)}
    user_msg.append(temp)
msg = input('请输入页码: ')
if msg.isdigit():
    for j in range((int(msg)-1)*10,int(msg)*10):
        print(user_msg[j])
else:
    print('内容格式错误')