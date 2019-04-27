# -*- encoding:utf-8 -*-
first = input('请输入密码: ')
password = '123456'
m = 1
while m < 3:
    if first != password:
        first = input('请重新输入: ')
        if m == 2:
            print("今日密码输入已达上限,请明天再试")
    else:
        print('密码正确')
    m = m + 1
