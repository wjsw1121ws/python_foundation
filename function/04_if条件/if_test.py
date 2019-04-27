# -*- encoding:utf-8 -*-

# if的使用
# if 条件:
#    执行的语句
# elif:
#    执行的语句
# else:
#    执行的语句

checkLogin = "1"
username = 'zhangsan'
password = '123456'

# if条件嵌套
if checkLogin == '1':
    # 并列条件: and, 或: or
    if username == 'zhangsan' and password == '123456':
        print('登陆成功! ')
    elif username != 'zhangsan' or password != '123456':
        print('登陆失败')
else:
    print('请输入登陆口令')

print('----------------------------------------------------')
service = input('请输入服务类型: ')

if service == '学生兼职':
    print('学生')
elif service == '丝袜诱惑':
    print('制服')
elif service == '性感女郎':
    print('性感')
else:
    print('少妇')

print('----------------------------------------------------')
if username == 'zhangsan':
    # pass: 表示不执行任何操作
    pass
