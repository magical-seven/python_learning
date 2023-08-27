# -*- encoding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test16_os.py
# @Time : 2023/8/25 10:30
# @Tool : PyCharm

# os 模块可以调用系统的相关函数模块
import os
'''
os.system('notepad.exe')   # 打开记事本
os.system('calc.exe')      # 打开计算器
os.startfile('E:\\wechat\\WeChat.exe')   # 打开微信
print(os.getcwd())
lst = os.listdir('../project_2023729')
print(lst)
# mkdir():创建目录，makedirs():创建多级目录，rmdir():删除目录，removeidrs():删除多级目录，chdir(path):将path设置为当前工作目录
os.makedirs('A/B/C')  # 创建多级目录
os.removedirs('A/B/C')  # 删除多级目录
'''
'''
"""
abspath(path):用于获取文件或目录的绝对路径；
exists(path):用于判断文件或者目录是否存在，如果存在返回True，否则返回false。
splitext()：分离文件名和扩展名；
basename(path):从一个目录中提取文件名；
dirname(path):从一个路径中提取文件路径，不包括文件名
os.path.isdir(path):用于判断是否为路径
"""
print(os.path.abspath('test16_os.py'))  # 返回绝对路径
print(os.path.exists('test16_os.py'),os.path.exists('testss'))   # 判断文件是否存在
print(os.path.join('D:\\python_ob\\project_2023729','test16_os.py'))  # 连接文件
print(os.path.basename('D:\\python_ob\\project_2023729\\test16_os.py'))
'''
'''
path = os.getcwd()
print(path)
lst = os.listdir(path)
# print(lst)
for filename in lst:
    if filename.endswith('.py'):
        # pass
        print(filename)
'''

path = os.getcwd()
lst_files = os.walk(path)  # DFS遍历目录以及相关的子目录，返回当前遍历的目录路径，子目录目录名（列表），当前目录下的文件（列表）
# print(lst_files)
# print(type(lst_files))
n = 1
for dirpath, dirname, filename in lst_files:
    # print(dirpath)
    # print(dirname)
    # print(filename)
    # print('---------')
    print('目录{0}'.format(n))
    if bool(dirname) == 0:
       print('None')
    else:
        for dir in dirname:
            print(os.path.join(dirpath, dir))
    print('文件')
    for file in filename:
        print(os.path.join(dirpath,file))
    n += 1



