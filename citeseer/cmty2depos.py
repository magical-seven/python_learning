pathc = './test2.txt'

with open(pathc,'r',encoding='gbk') as rf:
    lines = rf.readlines()
cmty_node = {}


for item in lines:
    item = item.replace('\n','')
    item = item.split('\t')
    item = [int(x) for x in item]
    cmty_node.setdefault(item[1], []).append(item[0])

cmty_node = dict(sorted(cmty_node.items()))

for key,value in cmty_node.items():
    cmty_node[key] = sorted(value)

# for key, values in cmty_node.items():
#     print(key)
#     print(values)
with open('cmty2.txt', 'w', encoding='gbk') as wf:
    for value in cmty_node.values():
        for item in value:
            wf.write(f"{item}\t")
        wf.write("\n")







