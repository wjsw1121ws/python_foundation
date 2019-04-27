#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: file_seek
    @Author: changchun_wu
    @Date: 2019/4/14 15:16
    @Version: 1.0 
"""

# seek使用
# 如果只有一个参数那么默认从最开的位置移动光标
# with open('../file/seek.txt','r+b') as file:
#     print(file.tell())      # 0
#     file.seek(10)
#     print(file.tell())      # 10
#     file.seek(2)
#     print(file.tell())      # 3

# 如果有第二个参数且为1,则表示从相对位置开始移动光标
# with open('../file/seek2.txt','rb') as file:
#     print(file.tell())      # 0
#     file.seek(10,1)
#     print(file.tell())      # 10
#     file.seek(3,1)
#     print(file.tell())      # 13

# 如果有第二个参数且为2,则从文件末尾开始读取
# with open('../file/seek3.txt','rb') as file:
#     print(file.tell())
#     file.seek(-6,2)
#     print(file.read())      # b'\r\n1111'

# 读取文件最后一行的内容
with open('../file/data_log','rb') as file:
    for line in file:
        skp = -10
        while True:
            file.seek(skp,2)
            file_readlines = file.readlines()
            if len(file_readlines)>1:
                print('最后一行的内容是: %s'%(file_readlines[-1]).decode('utf-8'))
                break
            skp*=2




