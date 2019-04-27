#!/usr/bin/env python
# -*- coding: utf-8 -*-
str
"""
  * @Description: 
  * @ClassName: 字符串
  * @Author: changchun_wu
  * @Date: 2019/3/25 16:22
  * @Version: 1.0 
"""
####字符串一旦创建无法修改

"""
    字符串常用的几个方法
    join        将字符串中的每个元素按照指定分隔符进行拼接
    split       风格字符串
    find        查询字符是否在字符串中
    strip       默认去掉字符串两边的空格,args: 移除指定字符---按照最多匹配的原则
    replace     替换字符串中的某些字符
    upper       转大写
    lower       转小写
"""

"""
    def capitalize(self, *args, **kwargs)
    将字符串的首字母大写
"""
print('首字符大写: capitalize()')
m = 'admin'  # str
n = m.capitalize()
print(n)
print('------------------------------')

"""
    casefold(self, *args, **kwargs)
    def lower(self, *args, **kwargs)
    将字符串中的大写字母转小写
    casefold()  --->可以处理特殊语言的大小写对应关系
    lower()     --->只能处理英文字母
    
"""
print('将字符串中的大写字母转小写: casefold()/lower()')
m = 'Admin'
n = m.casefold()  # 功能更强大---特殊语言的对应关系也可以处理
print(n)
n1 = m.lower()  # 只能处理英文
print(n1)
print('------------------------------')

"""
    def upper(self, *args, **kwargs)
    将字符串中的小写字母转大写
"""
print('将字符串中的小写字母转大写: upper()')
m = 'Admin'
print(m.upper())

"""
    def swapcase(self, *args, **kwargs)
    大小写字母互换---大写转小写,小写转大写
"""
print('大小写字母互换: swapcase()')
m = 'Admin'
print(m.swapcase())
print('------------------------------')

"""
    def center(self, width, fillchar=None)
    将字符串居中显示
    args1: 设置内容的总长度
    args2: 设置未占用的字符的填充, 默认是空格, 可自定义(只能是一个字符)
    return: 返回字符串(str)
"""
print('设置宽度并将内容居中: center()')
m = 'admin'
n = m.center(20)
print(n)
n1 = m.center(20, '-')
print(n1)
print('-----------------------------')

"""
    def ljust(self, *args, **kwargs)
    def rjust(self, *args, **kwargs)
    将字符串居左/右显示
    args1: 设置内容的总长度
    args2: 设置未占用的字符的填充, 默认是空格, 可自定义(只能是一个字符)
    return: 返回字符串(str)
"""
print('将字符串居左/右显示: ljust()/rjust()')
m = 'hello'
n = m.ljust(20, '-')
n1 = m.rjust(20, '-')
print(n)
print(n1)
print('-----------------------------')

"""
    def count(self, sub, start=None, end=None)
    统计字符串中某个字母出现的次数
    args1: 要统计的字母
    args2: 指定统计开始的索引
    args3: 指定统计该索引之前的内容
    return: 返回数字(int)
"""
print('统计字符串中某个字母出现的次数: count()')
m = 'helloworld'
n = m.count('l', 3, 8)
print(n)
print('-----------------------------')

"""
    def startswith(self, prefix, start=None, end=None)
    def endswith(self, suffix, start=None, end=None)
    判断字符串是否以指定字符开始/结尾
    args1: 要判断的参数
    args2: 指从指定索引开始判断
    args3: 指定统计该索引之前的内容
    return: 存在: True,不存在: False
"""
print('判断字符串是否以指定字符开始/结尾: startswith()/endswith()')
m = 'admin'
n = m.startswith('d', 1, 3)
print(n)
n1 = m.endswith('n', 1, 5)
print(n1)
print('-----------------------------')

"""
    def find(self, sub, start=None, end=None)
    查询字符是否在字符串中
    args1: 要查询的参数
    args2: 查询的起始索引
    args3: 查询指定索引之前
    return: 存在: 返回找到的第一个的索引,不存在: 返回-1
"""
print('查询字符是否在字符串中: find()')
m = 'admin'
n = m.find('m', 1, 3)
print(n)
print('-----------------------------')

"""
    def format(self, *args, **kwargs)
    格式化字符串: 将字符串中的占位符替换为指定的文本
"""
print('格式化字符串: format()')
m = 'i am {name} and i am {age}'
n = m.format(name='alex', age=18)
n1 = m.format_map({'name': 'john', 'age': 22})
print(n)
print(n1)
m2 = 'i am {0} and i am {1}'
n2 = m2.format('allen', 23)
print(n2)
print('-----------------------------')

"""
    def isalnum(self, *args, **kwargs)
    判断字符串是否只有字母和数字组成
"""
print('判断字符串是否只有字母和数字组成: isalnum()')
m = '!admin123456+'
n = m.isalnum()
print(n)
m = 'admin123456'
n = m.isalnum()
print(n)
print('-----------------------------')

"""
    def isalpha(self, *args, **kwargs)
    判断字符串是否只有字母组成
"""
print('判断字符串是否只有字母: isalpha()')
m = 'admin123456'
n = m.isalpha()
print(n)
print('-----------------------------')

"""
    def isalpha(self, *args, **kwargs)
    def isdecimal(self, *args, **kwargs)
    def isnumeric(self, *args, **kwargs)
    判断字符串是否只有数字组成
"""
print('判断字符串是否只数字: isdigit()/isdecimal()/isnumeric()')
m = '②'
n = m.isdigit()  # 支持特殊字符,但是不支持中文
n1 = m.isdecimal()  # 只支持十进制小数
n2 = m.isnumeric()  # 支持特殊字符,中文
print(n, n1, n2)
print('-----------------------------')

"""
    def expandtabs(self, *args, **kwargs)
    断句: 
        字符串中\t之前不足断句的长度,则会用tab空格补齐
        字符串中\t之前刚好满足断句的长度,则会用tab补齐六个空格
        字符串中\t之前大于断句的长度,则按断句长度向后数
    args1: 断句的长度
"""
print('断句:expandtabs()')
m = 'hello\tworld'
print(m, len(m))
n = m.expandtabs(10)
print(n, len(n))
print('-----------------------------')

"""
    def isidentifier(self, *args, **kwargs)
    判断字符串是否是标识符:
        标识符特征: 由字母,数字,下划线组成,数字不可以在前
"""
print('判断是否是标识符: isidentifier()')
m = 'abc_123'
n = m.isidentifier()
print(n)
print('-----------------------------')

"""
    def islower(self, *args, **kwargs)
    判断字符串是否都是小写--忽略字符串中的特殊字符和数字
    def isupper(self, *args, **kwargs)
    判断字符串是否都是大写--忽略字符串中的特殊字符和数字
"""
print('判断字符串是否都是小写/大写: islower()')
m = 'admin'
print(m.islower())
print(m.isupper())
print('-----------------------------')

"""
    def isprintable(self, *args, **kwargs)
    判断字符串中是否存在不可显示的字符(\n   \t)
    如果没有返回True,否则返回False
    \t 制表符
    \n 换行
"""
print('判断字符串中是否存在不可显示的字符: isprintable()')
m = 'hello\nworld'
n = m.isprintable()
print(n)
print('-----------------------------')

"""
    def isspace(self, *args, **kwargs)
    判断字符串是否由空格组成
"""
print('判断字符串是否由空格组成: isspace()')
m = '  \t   \n'
n = m.isspace()
print(n)
print('-----------------------------')

"""
    def title(self, *args, **kwargs)
    将字符串转化为标题----每个单词首字符大写
"""
print('将字符串转化为标题: title()')
m = 'Return True if the string is a title-cased string, False otherwise'
print(m.title())
print('-----------------------------')

"""
    def istitle(self, *args, **kwargs)
    判断字符串是否是标题
"""
m = 'Return True if the string is a title-cased string, False otherwise'
print(m.istitle())
n = m.title()
print(n.istitle())
print('-----------------------------')

"""
    def join(self, ab=None, pq=None, rs=None)
    将字符串中的每个元素按照指定分隔符进行拼接
"""
m = '你是风儿我是沙'
print(m)
print('--'.join(m))
print('-----------------------------')

"""
    def index(self, sub, start=None, end=None)
    获取字符串中某个字符第一次出现时的索引
    args1: 查询的字符
    args2: 从指定索引位置查询
    args3: 查询到指定索引
"""
print('获取字符串中某个字符第一次出现时的索引: index()')
m = 'helloworld'
n = m.index('o', 5, 10)
print(n)
print('-----------------------------')

"""
    def partition(self, *args, **kwargs)
    根据指定的分隔符将字符串进行分割---从左匹配
    def rpartition(self, *args, **kwargs)
    根据指定的分隔符将字符串进行分割---从右匹配
"""
print('根据指定的分隔符将字符串进行分割: partition()/rpartition')
m = 'a.dmi.n.add'
print(m.partition('.'))
print(m.rpartition('.'))
print('-----------------------------')

"""
    def split(self, *args, **kwargs)
    按照指定字符从左到右拆分
    args1: 拆分的规则
    args2: 按照规则拆分的个数 
    def rsplit(self, *args, **kwargs)
    按照指定字符从右到左拆分
    args1: 拆分的规则
    args2: 按照规则拆分的个数 
"""
print('拆分字符串: split()/rsplit()')
m = 'ad.m.in'
print(m.split('.', 1))
print(m.rsplit('.', 1))
print('-----------------------------')

"""
    def splitlines(self, *args, **kwargs)
    按照换行符进行分割
    args: 是否包含换行符--默认False
"""
print('按照换行符进行分割: splitlines()')
m = 'spl\nitli\nnes'
print(m.splitlines(True))
print(m.splitlines(False))
print('-----------------------------')

"""
    def strip(self, *args, **kwargs)
    默认去掉字符串两边的空格
    args: 移除指定字符---按照最多匹配的原则
    def lstrip(self, *args, **kwargs)
    去掉字符串左边的空格
    args: 移除指定字符---按照最多匹配的原则
    def rstrip(self, *args, **kwargs)
    去掉字符串右边的空格
    args: 移除指定字符---按照最多匹配的原则
"""
print('去掉字符串中的某个字符: strip()')
m = '  \nHelloWorld\t  '
n = 'admia'
print(m.strip(), n.strip('11miaa'))
print(m.lstrip(), n.lstrip('11miaa'))
print(m.rstrip(), n.rstrip('11miaa'))
print('-----------------------------')

"""
    def maketrans(*args, **kwargs)
    按照对应关系将字符串变为dict对象
    def translate(self, *args, **kwargs):
    将maketrans转换成的dict应用到指定字符串
"""
m = 'admin'
n = '12345'
v = 'orwnaaswlmgawonavlksdalj'
s = str.maketrans(m, n)
print(s)
print(v.translate(s))
print(str.translate(v, s))
print('-----------------------------')

"""
    def replace(self, *args, **kwargs)
    替换字符串中的某些字符
    args1: 被替换的字符
    args2: 替换成的字符
    args3: 替换的个数--没有参数默认全部替换
"""
print('替换字符串中的某些字符')
m = 'helllo'
print(m.replace('l', 'w'))
print(m.replace('l', 'w', 1))
print(m.replace('l', 'w', 2))
print('-----------------------------')
print('')
