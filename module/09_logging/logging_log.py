#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: logging_log
    @Author: changchun_wu
    @Date: 2019/4/28 3:18
    @Version: 1.0 
"""
    
import logging

def logger():
    logger = logging.getLogger()

    # 将log存放到文件
    file_handler = logging.FileHandler("./log/logger.log")
    # 将log打印在屏幕
    stream_handler = logging.StreamHandler()

    # 设置log的内容格式
    logging_formatter = logging.Formatter("%(lineno)d\t%(asctime)s\t%(message)s")

    # 将打印格式放入到文件处理器中
    file_handler.setFormatter(logging_formatter)
    stream_handler.setFormatter(logging_formatter)

    #
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(level=logging.DEBUG)

    return logger

logger = logger()

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')