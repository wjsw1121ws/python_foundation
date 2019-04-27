#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: file_
    @Author: changchun_wu
    @Date: 2019/4/13 23:35
    @Version: 1.0 
"""

# with open('../file/other.txt', 'r', encoding='gbk') as file:
#     # 获取文件打开时的编码
#     print(file.encoding)
#
#     # 将内容写入硬盘
#     file.flush()
#
#     # 获取光标所在的位置
#     print(file.tell())  # 0
#     file.readline()
#     print(file.tell())  # 5

    # read()默认按照字符的方式读取
    # print(file.read(3))

with open('../file/other.txt', 'r+', encoding='gbk') as file:
    # 截取文件内容
    file.truncate(10)