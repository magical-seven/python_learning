path_inter = './inter.txt'


# 跨层边集合
cross_01 = []
cross_02 = []

cross_10 = []
cross_20 = []

with open(path_inter,'r',encoding='gbk') as rf:
    interlines = rf.readlines()

r10 = interlines.index('=1,0=\n')
r20 = interlines.index('=2,0=\n')


for i, item in enumerate(interlines):
    if ("end" in item)|('=' in item):
        continue
    else:
        item = item.split('\t')[:2]
        item = [int(x) for x in item]

    if r10 < i < r20:
        cross_10.append(item)
        cross_01.append(item[::-1])
    elif i > r20:
        cross_20.append(item)
        cross_02.append(item[::-1])
    else:
        continue
# cross_01,cross_02,cross_12
# cross_10,cross_20,cross_21
cross = [cross_01,cross_10,cross_02,cross_20]

# for item in cross_01:
#     pass

# cross_10 = cross_01
Cross = {}
num = [12,21,13,31]
count = 0
for i,item in enumerate(num):
    Cross[item] = cross[i]
    count += 1

# for values in Cross[34]:
#     # print(key)
#     print(values)
#
# for values in Cross[43]:
#     # print(key)
#     print(values)
# print(len(Cross[12]))
# print(len(Cross[21]))


# print(cross_01)




