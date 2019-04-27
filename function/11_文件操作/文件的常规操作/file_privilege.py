#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: file_privilege
    @Author: changchun_wu
    @Date: 2019/4/13 1:07
    @Version: 1.0 
"""

# 文件的权限
# r---只读(默认值)
# with open('../file/test_file.txt', 'r', encoding='utf-8') as file:
#     print(file.readable())
#     print(file.writable())

# r---只写(默认值)
# with open('../file/test_file.txt', 'w', encoding='utf-8') as file:
#     print(file.readable())
#     print(file.writable())

# a--追加
# with open('../file/file_writer.txt', 'a',  encoding='utf-8') as file:
#     file.write('追加到最后')

# x--只写,文件存在则报错(FileExistsError)
# with open('../file/file_writer.txt', 'x',  encoding='utf-8') as file:
#     file.write('11')

# r+
# 可读可写
# 如果直接写则从光标最前面替代原文件中的内容插入
# 如果执行了操作则在光标最后面插入
# 如果文件不存在则报错
# with open('../file/file_writer.txt', 'r+', encoding='gbk') as file:
#     file.write('aa')
#     print(file.readable())
#     print(file.writable())
#     file.read()
#     file.write('bb')

# 模拟文件修改
# with open('../file/file_writer.txt','r',encoding='gbk') as file1, \
#     open('../file/file_writer1.txt','w',encoding='gbk') as file2:
#     file1_read = file1.readlines()
#     file2.write(file1_read[0])

# w+
# a+
# x+

# rb
# 使用rb方式是以二进制的方式打开文件,不能指定编码,会报错(ValueError)
# with open('../file/file_read_rb.txt','rb',encoding='utf-8') as file:
# with open('../file/file_read_rb.txt','rb') as file:
#     # file_read = file.read()
#     # 直接读取的是二进制字符
#     # print(file_read)
#     # 如果要将二进制字符变为字符串则需要解码
#     file_read_decode = file.read().decode('utf-8')
#     print(file_read_decode)

# wb
# with open('../file/file_writer_wb.txt','wb') as file:
#     # file.write(bytes('你好,1111',encoding='utf-8'))
#     file.write('你好,1111'.encode('utf-8'))

# ab
with open('../file/file_writer_wb.txt','ab') as file:
    # file.write(bytes('你好,1111',encoding='utf-8'))
    file.write('你好,22222'.encode('utf-8'))

# 模拟图片的复制
with open('../file/10.jpg','rb') as file1,open('../file/11.jpg','wb') as file2:
    data = file1.read()
    file2.write(data)

