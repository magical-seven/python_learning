"""
**Citesee**r[28]
来自一个学术搜索引擎，网站。
它包含一个研究者协作网络、一个论文引文网络和一个论文相似度网络。
该协作网络有3284个节点（研究人员）和13781条边（协作）。
论文引文网络有2035个节点（论文）和3356条边（论文引文）。
论文相似度网络有10214个节点（论文）和39411条边（内容相似度）。
交叉有三种类型：2634个协作引用关系，7173个协作相似度连接，2021个引用相似度边。
10个作者和论文的社区是基于研究领域的标记。
第0层是作者协作社区
第1层是论文引用网络
第2曾是论文相似度网络
"""
path_net = './networks.txt'
path_inter = './inter.txt'
path_cmty0 = './cmty0.txt'

# 每一层的层内节点总数
layer0_node = []
layer1_node = []
layer2_node = []


# 每一层的层内连边
layer0_link = []
layer1_link = []
layer2_link = []

# 第三层的权值列表
layer2_weight = []

# 层次划分
l0 = 0
l1 = 0
l2 = 0


with open(path_net,'r',encoding='gbk') as rf:
    lines = rf.readlines()[2:]

for i,item in enumerate(lines):
    if '#' in item:
        continue
    elif "--author--" in item:
        l0 = i
    elif '--citepp--' in item:
        l1 = i
    elif '--simpp--' in item:
        l2 = i


for i, item in enumerate(lines):
    if (i == l0) | (i == l1) | (i == l2):
        continue
    else:
        item = item.replace('\n','')
        item = item.split('\t')
        if i > l2:
            temp = item[2]
            item = [int(x) for x in item[:2]]
            item.append(temp)
        else:
            item = [int(x) for x in item[:2]]

    if l0 < i < l1:
        layer0_node.extend(item[:2])
        layer0_link.append(tuple(item[:2]))
    elif l1 < i < l2:
        layer1_node.extend(item)
        layer1_link.append(tuple(item))

    elif i > l2:
        layer2_node.extend(item[:2])
        layer2_link.append(tuple(item[:2]))
        layer2_weight.append(float(item[2]))



# 节点集合放入列表
layer0_node = sorted(set(layer0_node))
layer1_node = sorted(set(layer1_node))
layer2_node = sorted(set(layer2_node))



# print(layer2_weight[:10])
# 节点以及连接列表
layer_node = [layer0_node, layer1_node, layer2_node]
layer_link = [layer0_link, layer1_link, layer2_link]

# print(len(layer0_node))








