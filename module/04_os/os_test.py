#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: __init__.py
    @Author: changchun_wu
    @Date: 2019/4/24 23:36
    @Version: 1.0 
"""

import os

if __name__ == '__main__':

    # 获取当前的工作目录
    print(os.getcwd())

    # 修改当前工作目录
    os.chdir("test")
    print(os.getcwd())

    os.chdir('../')
    print(os.getcwd())

    # os.curdir()
    # print(os.getcwd())

    # 获取当前目录的父目录字符串名：('..')
    print(os.pardir)

    # 创建一级和多级目录
    # os.mkdir('./test1')
    # os.makedirs('./test2/test3')

    # 删除一级和多级目录(目录有文件不会删除该目录)
    # os.rmdir('test1')
    # os.removedirs('./test2/test3')

    # 列出指定路径下的所有文件(包括隐藏文件)
    print(os.listdir('./'))

    # 删除指定文件
    # os.remove('./.tt.txt')

    # 重命名文件或者文件夹
    # os.rename('./笔记.txt','./笔记bk.txt')
    # os.rename('./tt','./tt1')

    # 获取文件/目录信息
    print(os.stat('./test'))

    # 输出操作系统特定的路径分隔符，win下为"\",Linux下为"/"
    print(os.sep)

    # 输出当前平台使用的行终止符，win下为"\n",Linux下为"\n"
    print('start'+os.linesep+'end')

    # 输出用于分割文件路径的字符串 win下为;,Linux下为:
    print(os.pathsep)

    # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
    print(os.name)

    # 运行shell命令，直接显示
    # print(os.system('pwd'))

    # 获取系统环境变量
    print(os.environ)

    # 获取文件的绝对路径
    path = os.path.abspath('os_test.py')
    print(path)

    # 将path分割成目录和文件名二元组返回
    path_split = os.path.split(path)
    print(path_split)

    # 返回path的目录。其实就是os.path.split(path)的第一个元素
    print(os.path.dirname(path))

    # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
    print(os.path.basename(path))

    # 如果path存在，返回True；如果path不存在，返回False
    print(os.path.exists(path))

    # 如果path是绝对路径，返回True
    print(os.path.isabs('./os_test.py'))

    # 如果path是一个存在的目录，则返回True。否则返回False
    print(os.path.isfile('./os_test.py'))

    #  如果path是一个存在的目录，则返回True。否则返回False
    print(os.path.isdir('./os_test.py'))

    #  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
    join_path = os.path.join('C:\\a\\a\\a', 'b','c')
    print(join_path)

    # 返回path所指向的文件或者目录的最后存取时间
    print(os.path.getatime('os_test.py'))

    # 返回path所指向的文件或者目录的最后修改时间
    print(os.path.getctime('os_test.py'))

    # 返回path所指向的文件或者目录的创建时间
    print(os.path.getmtime('os_test.py'))

    # 返回path所指向的文件的大小
    print(os.path.getsize('os_test.py'))