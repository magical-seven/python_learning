# -*- encoding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test15_with.py
# @Time : 2023/8/24 22:03
# @Tool : PyCharm

# with 语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，以此来达到释放资源的目的
# 通过with来创建上下文管理器，实现了__enter__()和__exit__()两个特殊方法，__exit__()在上下文管理器中会自动调用，从而退出文档
'''
with open('c.txt','r',encoding='utf-8') as file:
    # file.read()
    file.readline
    file.seek(0)
    print(file.read())
'''

with open('613927.jpg','rb') as file1:
    # print(file1.read())
    with open('new.jpg','wb') as file2:
        file2.write(file1.read())    # 这里要写入其二进制文件

file = open('new.jpg','rb')
# print(file)
file.close()

