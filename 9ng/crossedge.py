path_inter = './inter.txt'


# 跨层边集合
cross_01 = []
cross_02 = []
cross_03 = []
cross_04 = []
cross_12 = []
cross_13 = []
cross_14 = []
cross_23 = []
cross_24 = []
cross_34 = []

cross_10 = []
cross_20 = []
cross_30 = []
cross_40 = []
cross_21 = []
cross_31 = []
cross_41 = []
cross_32 = []
cross_42 = []
cross_43 = []





with open(path_inter,'r',encoding='gbk') as rf:
    interlines = rf.readlines()

r01 = interlines.index('=0,1=\n')
r02 = interlines.index('=0,2=\n')
r03 = interlines.index('=0,3=\n')
r04 = interlines.index('=0,4=\n')
r12 = interlines.index('=1,2=\n')
r13 = interlines.index('=1,3=\n')
r14 = interlines.index('=1,4=\n')
r23 = interlines.index('=2,3=\n')
r24 = interlines.index('=2,4=\n')
r34 = interlines.index('=3,4=\n')



for i, item in enumerate(interlines):
    if ("end" in item)|('=' in item):
        continue
    else:
        item = item.split('\t')[:2]
        item = [int(x) for x in item]

    if r01 < i < r02:
        cross_01.append(item)
        cross_10.append(item[::-1])
    elif r02 < i < r03:
        cross_02.append(item)
        cross_20.append(item[::-1])
    elif r03 < i < r04:
        cross_03.append(item)
        cross_30.append(item[::-1])
    elif r04 < i < r12:
        cross_04.append(item)
        cross_40.append(item[::-1])
    elif r12 < i < r13:
        cross_12.append(item)
        cross_21.append(item[::-1])
    elif r13 < i < r14:
        cross_13.append(item)
        cross_31.append(item[::-1])
    elif r14 < i < r23:
        cross_14.append(item)
        cross_41.append(item[::-1])
    elif r23 < i < r24:
        cross_23.append(item)
        cross_43.append(item[::-1])
    elif r24 < i < r34:
        cross_24.append(item)
        cross_42.append(item[::-1])
    elif i > r34:
        cross_34.append(item)
        cross_43.append(item[::-1])
    else:
        continue
# cross_01,cross_02,cross_03,cross_04,cross_12,cross_13,cross_14,cross_23,cross_24,cross_34
# cross_10,cross_20,cross_30,cross_40,cross_21,cross_31,cross_41,cross_32,cross_42,cross_43
cross = [cross_01,cross_10,cross_02,cross_20,cross_03,cross_30,cross_04,cross_40,cross_12,cross_21,
         cross_13,cross_31,cross_14,cross_41,cross_23,cross_32,cross_24,cross_42,cross_34,cross_43]
for item in cross_01:
    pass




cross_10 = cross_01
Cross = {}
num = [12,21,13,31,14,41,15,51,23,32,24,42,25,52,34,43,35,53,45,54]
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