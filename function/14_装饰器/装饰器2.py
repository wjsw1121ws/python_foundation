#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    @Description: 
    @ClassName: 练习
    @Author: changchun_wu
    @Date: 2019/4/24 0:06
    @Version: 1.0 
"""
# def login(func):
#     def wrapper(*args,**kwargs):
#         username = input('请输入用户名: ').rstrip()
#         password = input('请输入密码: ').rstrip()
#         if username=='alex' and password=='123456':
#             res = func(*args,**kwargs)
#         return res
#     return wrapper

user_dict = [
    {'username':'alex','password':'123456'},
    {'username':'allen','password':'123456'},
    {'username':'johnson','password':'123456'},
    {'username':'justin','password':'123456'}
]

current_user = {'username':None,'user_login':False}

def login(file_type = 'file_db'):
    def user_check(func):
        def wrapper(*args,**kwargs):
            print(file_type)
            if file_type is 'file_db':
                if current_user['username'] and current_user['user_login']:
                    res = func(*args,**kwargs)
                    return res
                username = input('请输入用户名: ')
                password = input('请输入密码: ')
                for user in user_dict:
                    if username == user['username'] and password == user['password']:
                        current_user['username']  = username
                        current_user['user_login'] = True
                        res = func(*args, **kwargs)
                        return res
                else:
                    print('用户名或者密码错误')
            if file_type is 'mysql':
                print('鬼特么知道')
            if file_type is 'oracle':
                print('没学过')
        return wrapper
    return user_check

@login(file_type='file_db')
def index(name):
    print('%s欢迎来到主页'%name)

@login(file_type='mysql')
def home(name):
    print('%s欢迎回家' % name)

@login(file_type='oracle')
def cart(num,name):
    print('%s购物车的商品有%s个商品' % (name,num))

@login()
def order(product,price,num,name):
    print('%s购物车订单是: %s,%s,%s' % (name, product, price, num))

index('alex')
home('alex')
cart(10,'alex')
order('手机',1999,1,'alex')

