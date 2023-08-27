# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_12.py
# @Time : 2023/8/24 7:27
# @Tool : PyCharm

# 创建与使用模块

'''
import math
print(id(math))
print(dir(math))
'''
'''
from math import pi
print(pi)
'''

# 导入自定义模块
import test12_12_calc as calc
print(calc.add(2,3))
print(int(calc.div(9,3)))





