# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test8_string.py
# @Time : 2023/8/2 20:39
# @Tool : PyCharm

# 字符串和元组一样是不可变的序列
'''
a = 'python'
b = "python"
print(id(a),id(b))
'''
# 字符串的查询
'''
s = 'hello,hello'
# print(s.index('lo'))  # 首次出现的位置
# print(s.find('lo'))
# print(s.rfind('lo'))  # 最后一次出现的位置
# print(s.rindex('lo'))
# print(s.index('k'))  # ValueError: substring not found
# print(s.find('k'))  # -1 未查找到时候不会显示异常，返回-1
'''
# 字符串的大小写
'''
a = 'hello,python'
s=a.upper()
# print(id(s),'\t',id(a))
# print(s.lower())  # 转换之后会产生新的字符串
s1 = 'hello,Python'
print(s1.swapcase())  # 大写变小写，小写变大写
print(s1.title())
'''
# 字符串的对齐
'''
s = 'hello,python'
print(s.center(20,'*'))
# print(s.ljust(20,'*'))
print(s.rjust(10,"*"))  # 小于字符串长度则返回原字符串，不修改字符串
print(s.rjust(20,"*"))
print(s.zfill(20))  # 直接用0填充
print("-2938".zfill(10))
'''
# 字符串的分割
'''
s1 = 'hello python'
s = s1.title()  # 首字母大写
lst = s.split()   # 按照空格分割，并装入列表
print(lst,s)
'''
# 字符串的替换和合并 replace(),join()
'''
s = 'hello python'
lst = s.title()
lst = lst.replace('Python','Java')
lst = lst.replace(' ',',')
print(lst)
'''
# 字符串的比较
'''
# print("app">"apple") # 先比较长度，再逐字符比较
# print('apple'=='app')  # 对比
a = b ='app'
c = 'app'
print(a==b)
print(a==c)
print(a is b)
print(a is c)  # 字符串常量的驻留机制
print(id(a)," ",id(b),' ',id(c))
'''
# 字符串的切片操作
'''
s = 'hello,python'
s = s.title()
s1 = s[:5]  # [start:stop:step]
s2 = s[6:]
print(s1+'!'+s2)  # 切片操作产生新的字符串常量
print(s[::-1])  # 倒置，步长为负
'''
# 格式化字符串 占位符
'''
name = 'zhangsan'
age = 20
# print("my name is %s,my age is %d"%(name,age))
# print("my name is {0},my age is {1}".format(name,age))
# print(f'my name is {name},my age is {age}')
# print("%5d"%99)  # 宽度为5
print("%.3f"%3.1415926) # 保留小数点后三位(同c语言)
print('{0:.3}'.format(3.1415926)) # 保留三位数
print('{0:.3f}'.format(3.1415926))  # 保留三位小数
'''
# 字符串的编码转换
'''
s = '天涯共此时'
# 编码 encode
# print(s.encode(encoding="GBK")) # 在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding="UTF-8")) # 在UTF-8这种编码格式中，一个中文占三个字节
# 解码 byte代表就是一个二进制数据（字节类型数据）,编码就是将字符串变为二进制数据，解码是将二进制数据转变为字符串
byte = s.encode(encoding="GBK")  # 编码，解码
# byte = b'\xcc\xec\xd1\xc4\xb9\xb3\xb4\xcb\xca\xb1'
# byte1 = s.encode(encoding='UTF-8')
byte1 = b'\xe5\xa4\xa9\xe6\xb6\xaf\xe5\x85\xb1\xe6\xad\xa4\xe6\x97\xb6'  # 字符串的二进制码
# print(byte.decode(encoding="GBK"))  # 解码
print(byte1.decode(encoding='UTF-8'))
'''


