# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_6.py
# @Time : 2023/8/23 13:06
# @Tool : PyCharm

# 多态
class Animal(object):
    def eat(self):
        print('animal can eat')
class Dog(Animal):
    def eat(self):
        print('dogs have bones')
class Cat(Animal):
    def eat(self):
        print('cats have fish')

class Person:
    def eat(self):
        print('human hace rice')

def fun(obj):
    obj.eat()

# 动态语言的特点，可以直接调用类中的eat()
fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())


