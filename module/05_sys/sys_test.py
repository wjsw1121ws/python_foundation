#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: __init__.py
    @Author: changchun_wu
    @Date: 2019/4/24 23:36
    @Version: 1.0 
"""

import sys
import time

if __name__ == '__main__':
    # 命令行参数List，第一个元素是程序本身路径
    """
    λ python sys_test.py aaa abbbb
    ['sys_test.py', 'aaa', 'abbbb']
    """
    print(sys.argv)

    # 退出程序，正常退出时exit(0)
    def test():
        for i in range(1000):
            print(i)
            while i == 5:
                sys.exit()
    # test()

    # 获取Python解释程序的版本信息
    print(sys.version)

    # 获取最大int的值
    print(sys.maxsize)

    #  返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
    print(sys.path)

    # 向控制台打印, 可用于模拟进度条
    for i in range(100):
        time.sleep(0.5)
        sys.stdout.write('#')
        # sys.stdout.flush()