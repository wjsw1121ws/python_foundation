#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: sed
    @Author: changchun_wu
    @Date: 2019/4/25 1:24
    @Version: 1.0 
"""
import os


def query(data):
    # print('用户输入的数据是: %s'%data)
    backend_data = 'backend %s'%data
    with open('file/haproxy.conf','r',encoding='utf-8') as file:
        flag = False
        li = []
        for line in file:
            if line.rstrip() == backend_data:
                flag = True
                continue
            if flag:
                if line.startswith('backend'):
                    break
            if flag:
                print(line.rstrip())
                li.append(line)
    return li

def add(data):
    print('用户输入的数据是: %s' % data)
    print('添加之前内容是: ')
    res = query(data)
    with open('./file/haproxy.conf', 'r', encoding='utf-8') as file1, \
            open('./file/haproxy1.conf', 'w', encoding='utf-8') as file2:
        flag = False
        for line in file1:
            if line == res[-1]:
                # 该行读完并未做打印操作
                file2.write(line)
                flag = True
                continue
            if flag:
                input_text = input('请输入添加内容: ')
                file2.write('\t\t%s' % input_text+'\n')
                flag=False
            file2.write(line)
    change_name('./file/haproxy1.conf', './file/haproxy.conf')
    return '添加之后的内容是: %s'%query(data)

def change(data):
    print('用户输入的数据是: %s' % data)
    rr = query(data)
    for index, item in enumerate(rr):
        print('第' + str(index + 1) + '行', item, end='')
    line_num = input('请输入要修改的行号: ')
    print('要修改的原内容是: %s' % rr[int(line_num) - 1].rstrip())
    with open('./file/haproxy.conf', 'r', encoding='utf-8') as file1, \
            open('./file/haproxy1.conf', 'w', encoding='utf-8') as file2:
        if int(line_num) in list(range(1, rr.__len__() + 1)):
            for line in file1:
                # 表示找到了要修改的那一行
                if line == rr[-1]:
                    # 数据格式
                    # server 2.2.2.7 2.2.2.7 weight 30 maxconn 4000
                    user_input = input('请输入数据: ')
                    line = '\t\t%s' % user_input + '\n'
                file2.write(line)
    change_name('./file/haproxy1.conf','./file/haproxy.conf')
    return '修改之后的内容%s'%query(data)

def delete(data):
    print('用户输入的数据是: %s' % data)
    rr = query(data)
    for index, item in enumerate(rr):
        print('第' + str(index + 1) + '行', item, end='')
    line_num = input('请输入要删除的行号: ')
    print('要删除的原内容是: %s' % rr[int(line_num) - 1].rstrip())
    with open('./file/haproxy.conf', 'r', encoding='utf-8') as file1, \
            open('./file/haproxy1.conf', 'w', encoding='utf-8') as file2:
        if int(line_num) in list(range(1, rr.__len__() + 1)):
            for line in file1:
                # 表示找到了要修改的那一行
                if line == rr[int(line_num) - 1]:
                    line = ''
                file2.write(line)
    change_name('./file/haproxy1.conf', './file/haproxy.conf')
    return '删除之后的内容%s' % query(data)

# 定义文件修改
def change_name(original_name,new_name):
    os.remove(new_name)
    os.rename(original_name, new_name)

if __name__ == '__main__':
    msg = '''
    1:查询
    2:添加
    3:修改
    4:删除
    '''
    msg_dict = {
        '1':query,
        '2':add,
        '3':change,
        '4':delete
    }

    print(msg)
    while True:
        choice = input('请输入你的选项: ').rstrip()
        if not choice:
            continue
        if choice == '5':
            break
        data = input('请输入要查询的数据: ')
        res = msg_dict[choice](data)
        print(res)