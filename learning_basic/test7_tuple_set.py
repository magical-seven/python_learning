# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test7_tuple_set.py
# @Time : 2023/8/2 11:33
# @Tool : PyCharm


# 元组，不可变序列（还有字符串）[可变序列：列表和字典]
# 创建元组
'''
# t = ('da','dw','dqq','wdwa')
# t = 'da','dw','dqq','wdwa'
# print(t)
# t = tuple(('da','dw','dqq','wdwa')) #内置函数创建
print(t)
# 空列表
lst = []
lst = list()
# 空字典
dic = {}
dic = dict()
# 空元组
t = ()
t = tuple()
'''
# 元组中的列表
'''
t = (12,[23,32,34],11)
# t[1] = 'dase' #TypeError: 'tuple' object does not support item assignment
t[1].append(23)
print(t)
'''
# 遍历元组
'''
t = (12,[23,32,34],11)
for i in t:
    print(i)
'''

# 集合的创建
'''
# s = {'12','asd','adsd',123,'eqw','bendan'}  # 直接创建
# s1 = set({'12','asd','adsd',123,'eqw','bendan'})  #内置函数
s = set([1,23,4,5,31,2,3])   #集合无序
print(s)
#定义空集合
# s = {}  #空字典的定义
s = set()
print(s,type(s))
'''
# 集合的相关操作
# 集合的添加
'''
s = {'12','asd','adsd',123,'eqw','bendan'}
# s.add(80)
# print(s)
# s.update([233,433,533])
# s.update((233,433,533))
# s.update({233,433,533})
print(s)
'''
# 集合的删除
'''
s = set(range(21))
# for i in s:
#     print(set(i))
# print(list(s))
# s.remove(12) # 删除
# s.remove(100)  # KeyError: 100
# s.discard(11)
# s.discard(100) # 无报错
s.pop()
# s.pop(100) # TypeError: pop() takes no arguments (1 given)
s.clear()
print(s)
'''
# 集合的关系
'''
s = {1,2,3,4,5}
s1 = {5,4,3,2,1}
s2 = {1,2,3}
s3 = {1,2,7}
s4 = {123,23,12}
# print(s==s1)  # 无关顺序
# print(s.issubset(s2))
# print(s2.issubset(s))  # s2是否为s的子集
# print(s.issuperset(s1))   # s是否为s2的超集
# print(s.isdisjoint(s2))   # 是否没交集
# print(s.isdisjoint(s4))
'''
# 集合的数学操作
'''
s = {1,2,3,4,5}
s2 = {1,2,3}
s3 = {1,2,7}
s4 = {123,23,12}

# intersection()方法和 & 等价————————交集
# print(s.intersection(s3))
# print(s & s3)

# 并集操作
# print(s.union(s4))
# print(s| s4)

#差集操作
# print(s.difference(s2))
# print(s-s2)
'''
# 集合生成式
'''
s = {i for i in range(1,10)}
print(s)
'''





