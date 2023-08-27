# -*- coding:utf-8 -*-
# @Author : M.S
# @Project_Name : project_2023729
# @File_Name : test6_dict.py
# @Time : 2023/8/1 22:05
# @Tool : PyCharm

# 字典的创建
'''
# dict1 = {"张三":250,"李四":290}
dict1 = dict(张三=250,李四=290)  #内置函数创建字典
dict2 = dict({"张三":250,"李四":290})
print(dict1,dict2)
'''
# 字典的值的获取
'''
dict1 = {"张三":250,"李四":290}
# print(dict1["张三"])
# print(dict1["王五"])  #KeyError: '王五'
print(dict1.get('王五'))  #None
print(dict1.get('王五',99)) #改变不存在时输出的默认值为99
# print(dict1.get('张三'))
'''
# 字典的删除、新增和修改
'''
dict1 = {"张三":250,"李四":290}
# del dict1["张三"]
# dict1.clear()
dict1["王五"]=380  #新增元素
dict1["张三"]=380
print(dict1)
'''
# 字典视图
'''
dict1 = {"张三":250,"李四":290}
dict1['王五'] = 380
key = dict1.keys()
print(key)
value = dict1.values()
print(value)
item = dict1.items()
print(item)
print(dict1,"\t",list(key),"\t",list(value),"\n",list(item))    #list()转换为列表形式
'''
#字典元素的遍历
'''
dict1 = {"张三":250,"李四":290,"王五":380}
for item in dict1:
    print(item,dict1[item],dict1.get(item))
'''
# 字典生成式
'''
item = ["a","b","c","s"]
price = [90,20,30,12]
dic = {item.upper():price for item,price in zip(item,price)}
print(dic)
'''










