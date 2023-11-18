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


# 不同层的节点总数
layer0_node = []
layer1_node = []
layer2_node = []
layer3_node = []
layer4_node = []

# 不同层的连边
layer0_link = []
layer1_link = []
layer2_link = []
layer3_link = []
layer4_link = []


# 层次划分
l0 = 0
l1 = 0
l2 = 0
l3 = 0
l4 = 0

with open(path_net,'r',encoding='gbk') as rf:
    lines = rf.readlines()[2:]

for i,item in enumerate(lines):
    if '#' in item:
        continue
    elif "--0--" in item:
        l0 = i
    elif '--1--' in item:
        l1 = i
    elif '--2--' in item:
        l2 = i
    elif '--3--' in item:
        l3 = i
    elif '--4--' in item:
        l4 = i

for i,item in enumerate(lines):
    if (i == l0) | (i == l1)|(i == l2)|(i == l3)|(i == l4):
        continue
    else:
        item = item.split('\t')[:2]
        item = [int(x) for x in item]

    if l0 < i < l1:
        layer0_node.extend(item)
        layer0_link.append(tuple(item))
    elif l1 < i < l2:
        layer1_node.extend(item)
        layer1_link.append(tuple(item))
    elif l2 < i < l3:
        layer2_node.extend(item)
        layer2_link.append(tuple(item))
    elif l3 < i < l4:
        layer3_node.extend(item)
        layer3_link.append(tuple(item))
    elif i > l4:
        layer4_node.extend(item)
        layer4_link.append(tuple(item))


# 放入列表
layer0_node = sorted(set(layer0_node))
layer1_node = sorted(set(layer1_node))
layer2_node = sorted(set(layer2_node))
layer3_node = sorted(set(layer3_node))
layer4_node = sorted(set(layer4_node))
layer4_node.append(1200)  # 内部边连接不存在1200节点

# print(layer0_node)
# 节点以及连接列表
layer_node = [layer0_node, layer1_node, layer2_node, layer3_node, layer4_node]
layer_link = [layer0_link, layer1_link, layer2_link, layer3_link ,layer4_link]

# print(len(layer4_node))





