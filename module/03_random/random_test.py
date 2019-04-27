
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: random_test
    @Author: changchun_wu
    @Date: 2019/4/25 0:45
    @Version: 1.0 
"""
import random

# 取0-1的随机数(float)
print(random.random())

# 取1--100之间的随机数(int)
print(random.randint(1,100))

# 取1-3范围内的随机数
print(random.randrange(1,3))

# 随机从列表中取出一个元素
li = [22,"alex",False]
print(random.choice(li))

# 随机从列表中取出多个元素
print(random.sample(li,2))

# 从1-3中取任意浮点数
print(random.uniform(1,3))

# 打乱列表中元素的顺序
print(li)
random.shuffle(li)
print(li)
