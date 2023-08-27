# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_10.py
# @Time : 2023/8/24 6:56
# @Tool : PyCharm

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk


# 变量的赋值操作
'''
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)
'''
# 类的浅拷贝
cpu1 = CPU()
disk = Disk()
computer = Computer(cpu1,disk)

# 浅拷贝
import copy
computer2 = copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)   # 子对象都不拷贝，只拷贝了Computer的实例对象并为其创建对象

# 深拷贝
print('----------------------')
computer3 = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)   # 子对象也拷贝，递归拷贝所有对象





