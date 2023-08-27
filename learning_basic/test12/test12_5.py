# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_5.py
# @Time : 2023/8/23 12:58
# @Tool : PyCharm

# object类是所有类的父类，会自动继承object的属性和方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'my nama is {0},I\'m {1} years old'.format(self.name,self.age)   # 方法改写
stu = Student('zhangsan',20)
# print(dir(stu))
print(stu)  # 这里是自动调用__str__()方法（属于object的属性），显示该实例的基本信息





