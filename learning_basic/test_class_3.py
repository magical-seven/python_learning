# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test_class_3.py
# @Time : 2023/8/22 18:30
# @Tool : PyCharm

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):   # 实例方法
        print(self.name+"is eating now")

stu1 = Student('zhangsan',20)
stu2 = Student('lisi',30)

# 为stu2添加性别属性
stu2.gender = 'female'   # 动态绑定属性
# print(stu1.__dict__)
# print(stu2.__dict__)


# 动态绑定方法
def show():
    print("out of class")
stu1.show = show
# stu1.show()

'''
类对象（class）：类属性，类方法，实例方法，静态方法
实例对象：类名()创建实例对象，动态绑定属性，动态绑定方法
'''

















