from linklayer import layer_link
from cmtydeposition import Cmty
from crossedge import Cross


def static_cm(layer1:int,
              layer2:int,
              num1_cmty:int,
              num2_cmty:int,
              Cmty:list,
              Cross:dict,
              inter:bool=None):
    """
    :param layer1: 层号1(0,1,2)
    :param layer2: 层号2(0,1,2)
    :param num1_cmty: 社区编号  (1,2,3,4,5,6,7,8...28)
    :param num2_cmty: 社区编号  (1,2,3,4,5,6,7,8,...68)
    :param Cmty:层列表
    :param Cross:两层间的交叉边列表
    :return: count以及百分比
    """
    count = 0
    crossl = (layer1+1)*10 + (layer2+1)  # 交叉层层号
    for i in Cmty[layer1][num1_cmty]:
        for j in Cmty[layer2][num2_cmty]:
            if [i, j] in Cross[crossl]:
                count = count + 1
    cro_persent = count/len(Cross[crossl])
    # print(f"第{layer1}层的第{num1_cmty}社区与第{layer2}层的第{num2_cmty}社区连接的边数量为{count},占交叉边总数百分比为{cro_persent}")
    if inter: # 计算层内连接情况
        count_layer1 = 0
        count_layer2 = 0
        for i in Cmty[layer1][num1_cmty]:
            for j in reversed(Cmty[layer1][num1_cmty]):
                if i == j:
                    break
                if ((i,j) in layer_link[layer1]) or ((j,i) in layer_link[layer1]):
                    count_layer1 += 1

        for i in Cmty[layer2][num2_cmty]:
            for j in reversed(Cmty[layer2][num2_cmty]):
                if i == j:
                    break
                if ((i,j) in layer_link[layer2]) or ((j,i) in layer_link[layer2]):
                    count_layer2 += 1
        layer1_perinner = count_layer1 / len(layer_link[layer1])
        layer2_perinner = count_layer2 / len(layer_link[layer2])

        # print(
        #     f"第{layer1}层的第{num1_cmty}社区内部总边为{count_layer1},占本层边总数的{layer1_perinner}\n"
        #     f"第{layer2}层的第{num2_cmty}社区内部总边为{count_layer2},占本层边总数的{layer2_perinner}"
        # )
        return [count, cro_persent, count_layer1, count_layer2, layer1_perinner, layer2_perinner]
    else:
        return count,cro_persent


"""  
求最大连边数量和百分比
maxc, mcro_per = [0,0]
numcmty = [0,0]
for i in Cmty[0].keys():
    for j in Cmty[1].keys():
        tempc, tempcro_per = static_cm(0, 1, i, j,Cmty, Cross)
        if tempc > maxc:
            maxc = tempc
            mcro_per = tempcro_per
            numcmty = [i,j]

print(f"最大连边数量为{maxc},比例为{mcro_per},是0层{numcmty[0]}社区和1层{numcmty[1]}社区")

result:最大连边数量为319,比例为0.1211085801063022,是0层9社区和1层24社区


staticlst = static_cm(0, 1, 9, 24,Cmty, Cross, inter = True)
print(f"0层社区9 的内部边数量为{staticlst[2]},\t 占该层内部边百分比为{staticlst[4]} \n"
      f"1层社区24的内部边数量为{staticlst[3]},\t,占该层内部边百分比为{staticlst[5]}")
result
0层社区9 的内部边数量为7397,	 占该层内部边百分比为0.2683767505986503 
1层社区24的内部边数量为136,	,占该层内部边百分比为0.02026221692491061
"""

maxc, mcro_per = [0,0]
numcmty = [0,0]
for i in Cmty[0].keys():
    for j in Cmty[2].keys():
        tempc, tempcro_per = static_cm(0, 2, i, j, Cmty, Cross)
        if tempc > maxc:
            maxc = tempc
            mcro_per = tempcro_per
            numcmty = [i,j]

print(f"最大连边数量为{maxc},比例为{mcro_per},是0层{numcmty[0]}社区和1层{numcmty[1]}社区")





















