# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test14_encode&openfile.py
# @Time : 2023/8/24 16:57
# @Tool : PyCharm

'''
file = open('a.txt','r',encoding='utf-8')
print(file.readlines())
file.close()
'''
'''
file = open('b.txt','w',encoding='utf-8')
file.write('python')
file.close()

file = open('b.txt','a',encoding='utf-8')
file.write('\tpython')
file.close()
'''
'''
file = open('a.txt','r',encoding='utf-8')
print(file)
# print(file.read(2))
# print(file.read())
# print(file.readline())
print(file.readlines())
file.close()
'''

'''
file = open('a.txt','a',encoding='utf-8')
lst = ['java','python','go']
file.writelines(lst)
file.close()
'''
'''
file = open('c.txt','w',encoding='utf-8')
file.write('hellojavagopython')
file.close
 # utf-8编码下，一个中文字符占三个字节，
file = open('c.txt','r',encoding='utf-8')
file.seek(2)
print(file.read())
print(file.tell())  # 光标放置文件尾部
file.close()
'''
'''
a = '中国'
b = a.encode(encoding='utf-8')
c = a.encode(encoding='gbk')
print(a,b,c)
'''
with open('c.txt','r',encoding='utf-8') as file:
    print(file.readlines())    # 将每一行都放入列表


