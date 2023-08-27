# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_2.py
# @Time : 2023/8/23 8:58
# @Tool : PyCharm


class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age   # 在变量前加两个下划线，表示不希望在类外面被使用
    def show(self):
        print(self.name,self.__age)

stu = Student('zhangsan',30)
# stu.show()
# 在类外面使用name,age
# print(stu.name)
# print(stu.__age)
# print(dir(stu))  # 显示所有的属性和方法
print(stu._Student__age)  # 在类的外部可以通过 _Student__age进行方法




