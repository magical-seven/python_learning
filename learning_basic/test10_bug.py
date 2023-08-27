# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test10_bug.py
# @Time : 2023/8/21 22:47
# @Tool : PyCharm

import traceback

# 语法错误，类型错误，越界错误
# lst = []
# lst.extend(['a','w','d'])
# lst.insert(0,3)
# lst.insert(1,5)
# lst.insert(2,4)
# print(lst)

# bug的异常处理机制
'''
try:
    a = input('input one division:')
    b = input("input another division:")
    a = int(a)
    b = int(b)
    print(a/b)  # ZeroDivisionError
except ZeroDivisionError:
    print("ERROR")
except ValueError:
    print("ERROR")
print("program is over!")
'''

'''
try:
    a = int(input("one:"))
    b = int(input("another:"))
    result = a//b
except BaseException as e:
    print(e)
else:
    print(result)
'''

'''
try:
    a = int(input("one:"))
    b = int(input("another:"))
    result = a//b
except BaseException as e:
    print(e)
else:
    print(result)
finally:
    print("over")
'''

'''
ZeroDivisionError   # 除0错误
IndexError          # 索引不存在
KeyError            # 字典的键错误
NameError           # 未声明对象
SyntaxError         # python语法错误
ValueError          # 传入无效参数
'''

# traceback 模块打印异常
try:
    print("------")
    print(1/0)
except:
    traceback.print_exc()






