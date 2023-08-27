# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test12_13_calc2.py
# @Time : 2023/8/24 7:38
# @Tool : PyCharm


def add(a,b):
    return a+b

if __name__ == '__main__':    # 其他文件引入的时候，不会执行该句代码，只有运行本文件时（作为主程序时），才会执行该代码
    print(add(10,20))

