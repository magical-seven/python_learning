# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_4.py
# @Time : 2023/8/23 12:48
# @Tool : PyCharm

class Person(object):   # 默认Person继承object类（object类是所有类的父类）
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name," ",self.age)

class Student(Person): # 继承父类Person
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)   # 通过super()来调用父类的方法，将name和age传入
        self.stu_no = stu_no
    def info(self):
        super().info()    # 继承父类的方法
        print(self.stu_no)

class Teacher(Person):  # 继承父类Person
    def __init__(self,name,age,teachofyear):
        self.teachofyear = teachofyear
        super().__init__(name,age)
    def info(self):
        super().info()   # 方法重写，并继承父类的方法
        print(self.teachofyear)


stu = Student('zhangsan',20,'101')
# print(dir(stu))
teacher = Teacher('lisi',35,10)
stu.info()
teacher.info()







