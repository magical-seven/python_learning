# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test3.py
# @Time : 2023/7/30 13:48
# @Tool : PyCharm


#程序的组织结构：顺序，选择(if)，循环结构(while,for)
'''
#对象的布尔值：python一切都是对象，所有对象都有一个bool值，用bool()查看
# list = []
# print(bool(list))
# print(bool(None))
# print(bool(0))
# print(bool(False))
'''
#分支结构示例(if,elif,else)
'''
money = 100
s = int(input("输入取出的金额："))
if 0<=s<=money:
    money-=s
    print(money)
else:
    print("余额不足或输入有误")
'''
'''
num_a = int(input("NO.1:"))
num_b = int(input("NO.2:"))
print(str(num_a)+'小于等于'+str(num_b)  if num_a <= num_b else  str(num_a)+'大于'+str(num_b))
'''
# pass语句：什么都不做，只是一个占位符，用到需要写语句的地方。用于搭建代码结构和模块，测试语句是否有语法错误或其他逻辑错误
'''
answer = input("输入：(y/n)")
if answer == "y":
    pass
else:
    pass
'''







