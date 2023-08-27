# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_3.py
# @Time : 2023/8/23 10:32
# @Tool : PyCharm

# 继承，父类
class Person(object):   # 默认Person继承object类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name," ",self.age)

class Student(Person): # 继承父类Person
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)   # 通过super()来调用父类的方法，将name和age传入
        self.stu_no = stu_no

class Teacher(Person):  # 继承父类Person
    def __init__(self,name,age,teachofyear):
        self.teachofyear = teachofyear
        super().__init__(name,age)


stu = Student('zhangsan',20,'101')
# print(dir(stu))
teacher = Teacher('lisi',35,10)
stu.info()
teacher.info()




# 存在多继承
'''
class A:
    pass
class B:
    pass
class C(A,B):
    pass
'''