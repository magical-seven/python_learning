# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_8.py
# @Time : 2023/8/23 18:23
# @Tool : PyCharm

a = 20
b = 100
c = a+b
d = a.__add__(b)  # 加法本质就是调用__add__()方法
print(c,d)

class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self, other):    # 重写特殊方法
        return self.name+other.name
    def __len__(self):          # 重写特殊方法
        return len(self.name)


'''
stu1 = Student('zhangsan')
stu2 = Student('lisi')
print(stu1+stu2)   # 调用Student类中的__add__()的方法
s = stu1.__add__(stu2)
print(s)
print(len(stu1))
'''












