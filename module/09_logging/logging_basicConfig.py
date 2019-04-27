#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: logging_test
    @Author: changchun_wu
    @Date: 2019/4/28 2:51
    @Version: 1.0 
"""
import logging

"""
    format参数中可能用到的格式化串：
    %(name)s Logger的名字
    %(levelno)s 数字形式的日志级别
    %(levelname)s 文本形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s 调用日志输出函数的模块名
    %(funcName)s 调用日志输出函数的函数名
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    %(message)s用户输出的消息                        
"""


logging.basicConfig(
    # 设置log级别
    level=logging.DEBUG,
    # 设置log存储位置
    filename="./log/logger.log",
    # 设置log的写入方式
    filemode="w",
    # 设置显示的参数
    format="%(lineno)d\t%(asctime)s\t%(message)s",

)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')