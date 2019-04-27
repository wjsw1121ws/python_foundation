#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: re_test
    @Author: changchun_wu
    @Date: 2019/4/27 16:40
    @Version: 1.0 
"""
import re

# 字符：. ^ $ * + ? { } [ ] | ( ) \

if __name__ == '__main__':
    # 通配符匹配.
    print(re.findall("a..x", "awexwqalexwrerq"))

    # 从开头匹配^
    print(re.findall("^a..x", "awexwqalexwrerq"))

    # 从结尾匹配$
    print(re.findall("a..x$", "awerwqalexwalex"))

    # 匹配(0,+oo) *
    print(re.findall("alex*", "asdfsfale"))
    # 匹配(1,+oo) +
    print(re.findall("alex+", "asdfsfale"))
    # 匹配(0,1) ?
    print(re.findall("alex?", "asdfsfalexxxx"))
    print(re.findall("alex?", "asdfsfale"))
    # *,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配
    print(re.findall("alex*?", "asdfsfalexxxxxx"))

    # 自定义匹配个数 {x,y}
    print(re.findall("alex{0,2}", "asdfsfalexxxx"))

    # []的使用
    # 匹配其中的任意一个,括号中可以的正则符号有,^(非),-(从-到),\()
    print(re.findall("x[yz]", "xyyyxzzz"))
    print(re.findall("x[a-z]", "xxabcxddd"))
    print(re.findall("x[a-z]*", "dafaxfafafa9"))
    print(re.findall("x[0-9]*", "dafax76845fafafa9"))
    print(re.findall("x[^0-9]*", "dafaxsfaf76845fafafa9"))

    # \的使用
    """
    \d  匹配任何十进制数；它相当于类 [0-9]。
    \D 匹配任何非数字字符；它相当于类 [^0-9]。
    \s  匹配任何空白字符；它相当于类 [ \t\n\r\f\v]。
    \S 匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
    \w 匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
    \W 匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]
    \b  匹配一个特殊字符边界，比如空格 ，&，＃等
    """

    # 转义符的使用
    print(re.findall("www\.baidu\.com", "www.baidu.com"))
    print(re.findall("e\\\\g", "ade\g"))
    print(re.findall(r"e\\g", "ade\g"))

    # \b的使用
    print(re.findall("I\\b", "I am I ACID"))

    # | 匹配任意一个
    print(re.findall("af|qt", "sfafffdaweqtqkgi"))

    # ()分组
    print(re.findall("(abc)+", "abcdabcdabcd"))

    # 12+(34*36+2-5*(2-1))
    print(re.findall("\([^()]*\)", "12+(34*36+2-5*(2-1))"))

    # finditer
    res = re.finditer("(abc)+", "abcdabcdabcd")
    res_next = res.__next__()
    print(res_next.group(),"-----")

    # search 分组
    print(re.search("(?P<name>[a-z]+)(?P<age>\d+)", "alex32allen24").group())
    print(re.search("(?P<name>[a-z]+)(?P<age>\d+)", "alex32allen24").group("name"))

    # match 只会从开头匹配
    print(re.match("\d+", "allen111"))
    print(re.match("\d+", "32alex").group())

    # split 正则分割(左边没有内容则为空)
    print(re.split("\s","192 168 25 133"))
    print(re.split("\.","192.168.25.133"))
    print(re.split("\\\\","192\\168\\25\\133"))
    print(re.split('[ab]', "abc"))

    # 正则替换
    print(re.sub("\d+", "R", "ww666cc"))
    print(re.sub("\d", "R", "ww666cc",2))

    # 显示替换的个数
    print(re.subn("\d", "R", "ww666cc"))

    # 定义正则规则
    re_compile = re.compile("\d+")
    print(re_compile.findall("afaf5555sfaf11e"))

    # 注意点,分组优先得到的是分组的内容
    print(re.findall("www\.(baidu|sina)\.cn", "www.baidu.cn"))
    # 通过?:取出优先级
    print(re.findall("www\.(?:baidu|sina)\.cn", "www.baidu.cn"))
    print(re.findall("(?:abc)+", "abcabcabc"))

