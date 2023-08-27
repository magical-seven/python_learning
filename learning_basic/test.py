# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test.py
# @Time : 2023/7/29 16:20
# @Tool : PyCharm

import keyword

'''
#print (文件输出)
# a+表示文件不存在则创建，存在就在文件内容后面追加，注意转义字符
fd = open('D:\\python_ob\\project_2023729\\test.txt','a+') 
print('hello', file=fd)
fd.close()
'''

#转移字符、原字符（使得转移字符不起作用，在字符串前加r或者R）
'''
print("http:\\\\www.baidu.com")
print(r"http:\\www.baidu.com") #最后一个字符不能是”\ “
'''

#保留字和标识符
'''
#print(keyword.kwlist) #打印保留字
'''

#变量名
'''
name = 'magic-seven'
#id()打印变量存储的地址，type()打印变量的类型
print("name:",id(name),type(name))
name_address = hex(id(name))
print("十六进制地址：",name_address)
'''

#进制
'''
print('二进制',0b1010)
print('八进制',0o1010)
print('十六进制',0x1010)
'''

#浮点数不精确处理
'''
from decimal import Decimal
print(2.2+1.1)
print(Decimal('2.2')+Decimal('1.1'))
'''

#数据类型的强行转换//int()\float()\str()
'''
age = 20
age_str = str(age)
# print(type(age),type(age_str))
print("我的年龄是："+age_str+"岁")
'''



