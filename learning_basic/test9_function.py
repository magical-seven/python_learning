# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test9_function.py
# @Time : 2023/8/15 16:38
# @Tool : PyCharm

# 函数的调用
'''
def calc(a,b):  # 形参
    c = a+b
    return c

# x = calc(20,123)  # 实参（位置传参）
# print(x)

# 函数的参数传递
# x = calc(b=10, a=20)  # 关键字传参
print(x)
'''

# 函数的参数传递
'''
def fun(arg1, arg2):
    print("arg1=",arg1)
    print("arg2=",arg2)
    arg1 = 100
    arg2.append(10)
    print("arg1=", arg1)
    print("arg2=", arg2)

n1 = 11
n2 = [22,33,44]
print(n1)
print(n2)
# print('\n')
fun(n1,n2)  # 位置传参
print(n1)
print(n2)
"""
在函数调用过程中，进行参数的传递：
如果是不可变对象，在函数体的修改不会影响实参的值
如果是可变对象，在函数体的修改会影响到实参的值
"""
'''

# 函数的返回值，多个返回值时，结果为元组
'''
def fun(num):
    odd = []
    even = []
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
print(fun([12,3,23,4,231,233,25,4675,237,83,8844,74]))   # 打印为元组
'''

# 函数参数
'''
def fun(*args):   # 个数可变的位置形参
    print(args)   # 以元组形式打印

def fun2(**arg2):  # 个数可变的关键字形参
    c = []
    d = []
    for i in arg2.values():
        c.append(i)
    for j in arg2.keys():
        d.append(j)
    print(d,c)
    print(type(arg2))
    # print(arg2)   # 以字典形式打印

# fun(10,201,10,32,43)   # 元组(位置实参传递)
# fun2(a=231,b=23,c=66,d=232)   # 字典(关键字是实参传递)

def fun3(a,b,*,c,d):   # 在*之后，所有的实参传递都必须是关键字实参传递。
    print('a=',a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

# fun3(12,32,c=21,d=22)

def fun4(a,b,c=10,*arg,d,e,**args):
    pass
def fun5(a,b,*,c,**qargs):
    pass
def fun6(*args,**kwargs):  # 多个位置形参和多个关键字形参
    pass
'''

# 函数变量
'''
def fun(a,b):
    c = a+b
    print(c)   # c和a,b都是局部变量

name = 'yang'  # 全局变量
def fun2():
    print(name)
# fun2()
def fun3():
    global age   # 将age变为全局变量
    age = 20
    print(age)
# fun3()
print(age)
'''

# 递归函数
'''
def fun(n):   # 简单递归函数
    if n == 1:
        return 1
    else:
        return fun(n-1)*n
c = fun(6)
print(c)
'''
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))
































