#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 练习
    @Author: changchun_wu
    @Date: 2019/4/25 1:03
    @Version: 1.0 
"""

# 随机生成一个六位数的验证码,包括字母和数字
import random


def vcode():
    res = ''
    for i in range(5):
        randint = random.randint(0, 9)
        randstr1 = chr(random.randint(65, 90))
        randstr2 = chr(random.randint(97, 122))
        random_choice = random.choice([randint, randstr1,randstr2])
        res += str(random_choice)
    return res

if __name__ == '__main__':
    for i in range(10):
        print(vcode())
