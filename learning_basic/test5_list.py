# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test5_list.py
# @Time : 2023/7/31 12:05
# @Tool : PyCharm


# 列表创建的两种方法
'''
list1 = ["11","22","33"]
list2 = list(["11","22","33"])
print(list2,list1[1],list1[-2],id(list1),id(list2))
'''
# 列表的索引方法
'''
lst = ["hello","edhwio","dsde","sdas","hello"]
print(lst.index("hello")) #返回第一个查找的值的列表值
print(lst.index('hello',1,5))
print(id(lst[1]),id(lst[2]),id(lst[3]))
'''
# 切片操作 切片的结果：列表的部分，切片的范围：[start,stop)
'''
lst = [2,23,42,123,43,232,222,31,29]
lst1 = lst[1:5:1]
print(lst,"\t",lst1)
'''
# 列表的增删改查：
'''
# append(),extend(),insert(),切片，列表的添加
lst = [2,3,23,4,5,6,7,8,9,12,32,54]
# print(lst,id(lst))
# lst.append(100)
# print(lst,id(lst))
lst2 = ["hhh","dasdw"]
# lst.append(lst2)  #在列表末尾添加一个元素，将lst2作为一个元素
# print(lst)
# lst.extend(lst2)  #可在列表添加多个元素，lst2中每个元素作为一个元素添加到lst中
# print(lst)
# lst.insert(1,lst2)
# print(lst)
# 切片方法添加元素，同insert()方法对比
n = 3
lst[n:]=lst2
print(lst)
'''
#列表的删除
'''
#remove(),pop(),切片,clear(),del
lst = [2,3,23,4,5,6,7,8,9,12,32,54]
lst2 = ["hhh","dasdw"]
# lst.remove(54)  # 删除指定元素
# print(lst)
# lst.pop(3) # 删除指定位序的元素
# print(lst)
# lst.pop()
# lst3 = lst[0:5] #切片删除
# lst[0:5] = []  #不产生新的列表
# lst.clear() # 删除所有元素
# print(lst)
# del lst  # 删除列表对象
print(lst)
'''
#列表的修改
'''
lst = [2,3,23,4,5,6,7,8,9,12,32,54]
lst2 = ["hhh","dasdw"]
# lst[2] = 34
# lst[1:5] = [12,32,42,21,12,23]  #切片修改
print(lst)
'''
#列表的排序
'''
lst = [2,3,23,4,5,6,7,8,9,12,32,54]
lst2 = ["hhh","dasdw"]
# print(lst)
# lst.sort()   #默认升序，reverse=true表示降序
# print(lst)
# lst.sort(reverse=True)   # 降序排序
# print(lst)
asc_lst3 = sorted(lst)  # 内置函数
desc_lst = sorted(lst,reverse=True)
print(asc_lst3,"\n",desc_lst)
'''
#列表的生成
'''
lst = [i for i in range(10)]
lst_2 = [i**2 for i in range(10)]
lst_3 = [i*2 for i in range(1,6)]
print(lst,"\t",lst_2,"\t",lst_3)
'''






