#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: file_
    @Author: changchun_wu
    @Date: 2019/4/12 23:34
    @Version: 1.0 
"""

# idea创建的文件为UTF-8,在打开文件使用的windows的默认编码(GBK),所以不指定文件打开时的编码会报错(UnicodeDecodeError)
# 逐行读取
# with open('../file/test_file.txt') as file:
# with open('../file/test_file.txt', encoding='utf-8') as file:
#     for line in file:
#         print(line.rstrip())

# readlines默认读取所有内容,将每行的内容作为一个元素放入到列表中
# with open('../file/test_file.txt',encoding='utf-8') as file:
#     file_readlines = file.readlines()
#     # print(file_readlines)
#     # 逐行输出列表中的内容需要使用for循环
#     for readline in file_readlines:
#         # 由于print方法会有换行符,所以要用rstrip()去除右边的空格
#         print(readline.rstrip())

# readline逐行读取(默认读取一行)
# with open('../file/test_file.txt',encoding='utf-8') as file:
#     file_readline = file.readline()
#     # 读取一行记录
#     print('第一行', file_readline)      # 第一行
#     print('第二行', file_readline)      # 第二行
#     # 参数默认值为-1,读取一行,如果设置参数表示读取一行的多少字符
#     readlines = file.readline(5)
#     print(readlines)

# 调用read()方法会默认读取全部内容
# with open('../file/test_file.txt', encoding='utf-8') as file:
#     file_read = file.read()
#     print(file_read)
#     file.close()



# 文件路径
# 相对路径
# with open('../file/test_file.txt', 'w', encoding='utf-8') as file:
# 绝对路径
# with open('D:\\Python\\01-python基础\\src\\com.wcc.python\\11_文件操作\\file\\test_file.txt', encoding='utf-8') as file:
with open('D:/Python/01-python基础/src/com.wcc.python/11_文件操作/file/test_file.txt', encoding='utf-8') as file:
    for line in file:
        print(line.rstrip())


