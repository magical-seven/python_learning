# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_9.py
# @Time : 2023/8/23 18:34
# @Tool : PyCharm

class Person:

    def __new__(cls, *args, **kwargs):        # __new__用于创建对象
        print("__new__被调用执行了，cls的id值为{0}".format(id(cls)))
        obj = super().__new__(cls)
        print('__new__创建的对象id为{0}'.format(id(obj)))
        return obj                           # 返回所创建的对象

    def __init__(self,name,age):             # self就是创建的对象，__init__对创建的对象初始化
        print("__init__被调用了，self的id值为{}".format(id(self)))
        self.name = name
        self.age = age

print('object类对象的id为{0}'.format(id(object)))
print('Person类对象的id为{0}'.format(id(Person)))


p1 = Person('zhangsan',20)
print('p1这个Person的类的实例对象的id为{0}'.format(id(p1)))





