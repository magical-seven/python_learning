# -*- encoding:utf-8 -*-
# @Author : M.S
# @Project_Name : 6ng
# @File_Name : nodecmty.py
# @Time : 23:47
# @Tool : PyCharm

"""
是由20个新闻组数据集构建的两个多域网络数据集。
6NG包含5个大小为{600、750、900、1050、1200}的网络
9个NG由5个大小为{900、1125、1350、1575、1800}的网络组成。
节点表示新闻文档，而边缘描述了它们的语义相似性。交叉网络关系由两个网络的两个文档之间的余弦相似度来衡量。
在6个NG和9个NG的5个网络中的节点分别从6个和9个新闻组中选择。每个新闻组都被认为是一个社区。
"""
path_net = './networks.txt'
path_inter = './inter.txt'
path_cmty0 = './cmty0.txt'
path_cmty1 = './cmty1.txt'
path_cmty2 = './cmty2.txt'
path_cmty3 = './cmty3.txt'
path_cmty4 = './cmty4.txt'




