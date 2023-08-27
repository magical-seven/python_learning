# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test_class_1.py
# @Time : 2023/8/21 23:51
# @Tool : PyCharm

class Student:
    native_pace = 'jilin'
    def __init(self,name,age):
        self.name = name       # self.name称为是实体属性，进行的是一个赋值操作，将局部变量name的值赋给实体属性
        self.age = age

    def eat(self):   # 实例方法
        print(self.age,' ',self.name)

    @staticmethod
    def method():    # 静态方法，不写self，用staticmethod修饰
        print("static method")

    @classmethod
    def cm(cls):   # 类方法，用classmethod修饰，传递cls
        print('class method')

print(id(Student))
print(type(Student))
print(Student)







