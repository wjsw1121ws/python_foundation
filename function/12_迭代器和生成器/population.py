#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: population
    @Author: changchun_wu
    @Date: 2019/4/15 22:48
    @Version: 1.0 
"""


def get_population():

    with open('./people.txt', 'r', encoding='utf-8') as file:
        for line in file:
            yield line

gg = get_population()
next__ = gg.__next__()
xx = eval(next__)
print(xx['population'],type(xx))

# 求总人口
all_population = sum(eval(gg)['population'] for gg in get_population())
print(all_population)

# 求某个省份的人口占比
# ('省份: %s, 人口占比: %2.f' )
print(eval(get_population().__next__())['city'],
      eval(get_population().__next__())['population']/all_population)

print('城市: ',(eval(gg)['city'] for gg in get_population()).__next__())
print('人口占比: ',(eval(gg)['population']/all_population for gg in get_population()).__next__())

