# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test_class_2.py
# @Time : 2023/8/22 18:04
# @Tool : PyCharm

# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test_class_1.py
# @Time : 2023/8/21 23:51
# @Tool : PyCharm

class Student:
    native_pace = 'jilin'    # 直接写在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name = name       # self.name称为是实体属性，进行的是一个赋值操作，将局部变量name的值赋给实体属性
        self.age = age

    def eat(self):
        print('chifan')

    @staticmethod
    def method():    # 静态方法，不写self，用staticmethod修饰
        print("static method")

    @classmethod
    def cm(cls):   # 类方法，用classmethod修饰，传递cls
        print('class method')

# print(id(Student))
# print(type(Student))
# print(Student)

# 创建Student对象
'''
stu = Student('zhangsan',23)    # 实例对象
stu.eat()
Student.eat(stu)  # 代码执行功能与stu.eat()相同
print(stu.age)
print(stu.name)
# print(id(stu))
# print(type(stu))
# print(stu)
'''

# 类属性   类属性是归所有该类别的实例对象所共享的
'''
print(Student.native_pace)
stu1 = Student('zhangsan',20)
stu2 = Student('lisi',23)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = 'tianjing'
print(stu1.native_pace)
print(stu2.native_pace)   
'''

# 类方法
Student.cm()
Student.method()




