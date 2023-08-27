# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_7.py
# @Time : 2023/8/23 15:14
# @Tool : PyCharm

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
class D(A):
    pass



# 创建C类的对象
x = C('jack',20)
print(x.__dict__)  # 实例对象的属性字典
# print(dir(x))
# print(C.__dict__)
print(x.__class__)  # 输出对象所属的类
print(C.__bases__)   # C类父类类型的元组
print(C.__base__)  # 输出C类父类类型中一个(基类)
print(C.__mro__)  # 输出类的层次结构
print(A.__subclasses__())  # 输出子类的列表





