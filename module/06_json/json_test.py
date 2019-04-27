#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    #!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
import json

dic = {'name':'alex','age':28}
# 将对象变为json字符串---序列化操作
# 把对象(变量)从内存中变成可存储或传输的过程称之为序列化
json_dumps = json.dumps(dic)
print(json_dumps,type(json_dumps))

# 将字符串变为对象----反序列化
# 把变量内容从序列化的对象重新读到内存里称之为反序列化
json_load = json.loads(json_dumps)
print(json_load,type(json_load))

# dump用户文件处理,有两个参数,第一个是对象,第二个是文件打开的文件名
dic = {'name':'alex','age':28}
with open('test','w',encoding='utf-8') as file:
    json.dump(dic, file)

# load
with open('test','r',encoding='utf-8') as file:
    json_load = json.load(file)
    print(json_load,type(json_load))
