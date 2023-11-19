path_cmty0 = './cmty0.txt'
path_cmty1 = './cmty1.txt'
path_cmty2 = './cmty2.txt'


Path = [path_cmty0,path_cmty1,path_cmty2]


# 每一层的社区
layer0_cmty = {}
layer1_cmty = {}
layer2_cmty = {}

Cmty = [layer0_cmty,layer1_cmty,layer2_cmty]

for i ,path_p in enumerate(Path):
    with open(path_p, 'r', encoding='gbk') as rf:
        cmtylines = rf.readlines()

    for j, item in enumerate(cmtylines):
        item = item.split('\t')
        item = item[:-1]
        item = [int(x) for x in item]
        Cmty[i][j+1] = item


# for key,value in layer2_cmty.items():
#     print(key)
#     print(value)








