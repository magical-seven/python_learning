# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test4.py
# @Time : 2023/7/30 18:38
# @Tool : PyCharm


#range()
'''
# r = range(10)
# print(type(r))
# print(list(r))
# for i in r:
#     print(i)

r = range(1,10)
print(list(r))

r = range(1,10,2)
print(list(r))
print(10 in r)
print(9 in r)

print(list(range(1,10,1)))
'''

# 计算1-100之间的偶数和
'''
sum = 0
for i in range(0,101,2):
    sum+=i
print(sum)

for item in 'python':
    print(item)
'''
# 简单示例：枚举水仙花数
'''
for i in range(100,1000):
    a = i%10
    b = (i%100)//10
    c = i//100
    if i == a**3+b**3+c**3:
        print(i)
'''

# else语句
'''
password = '888'
for i in range(3):
    pwd = input("input your password:")
    if pwd == password:
        print("true!")
        break
    else:
        print("False,please reinput!")
else:
    print("the secret is false!")  #这里的else与for搭配，也可以while循环搭配
'''

# 输出一个三行四列的矩阵
'''
for i in range(3):
    for j in range(4):
        print("*",end="")  #不换行输出 end=""
    print("") #print()自动换行
'''

# 九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="\t")
    print()
'''

#break:退出本轮循环；continue:退出本次循环







