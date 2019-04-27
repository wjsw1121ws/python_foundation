#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: test
    @Author: changchun_wu
    @Date: 2019/4/25 2:43
    @Version: 1.0 
"""

# with open('file/haproxy.conf','r',encoding='utf-8') as file:
#     # readlines = file.readlines()
#     for item in file:
#         print(item)

li = [1,2,3,4]
# print(li.__len__())
# print()
# l = list(zip(range(1,li.__len__()+1),['alex', 'allen', 3]))
# print(l)
# print(l[0][1])
# print(list(range(2)))
li = ['1111111','2222222','3333333']
with open('./file/ff.txt','r',encoding='utf-8') as file:
    for line in file:
        if line==li[-1]:
            print(line)