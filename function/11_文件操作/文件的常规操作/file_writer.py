#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: file_writer
    @Author: changchun_wu
    @Date: 2019/4/13 0:39
    @Version: 1.0 
"""
# 写操作--要赋予写操作,文件内容只能是字符串
# writer(),以字符串的方式写入文件中,每次写入都会覆盖文件内容
# with open('../file/file_writer.txt', 'w',  encoding='utf-8') as file:
# #     file.write('第一行\n第二行\n')
# #     file.write('第三行')
#     file.close()
#     # 文件关闭后无法读写
#     # file.write('11')

# writelines()--将每行内容放入列表中写入
# with open('../file/file_writer.txt', 'w',  encoding='utf-8') as file:
#     file.writelines(['第一行\n','第二行\n','第三行\n'])
#     file.close()

