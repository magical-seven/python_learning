from linklayer import layer_link
from cmtydeposition import Cmty
from crossedge import cross_01,cross_02,cross_03,cross_13,cross_04,cross_12,Cross


def static_cm(layer1:int,
              layer2:int,
              num1_cmty:int,
              num2_cmty:int,
              Cmty:list,
              Cross:dict,
              inter:bool=None):
    """
    跨层连接的统计
    :param layer1: 层号1(0,1,2,3,4,5)
    :param layer2: 层号2(0,1,2,3,4,5)
    :param num1_cmty: 社区编号(1,2,3,4,5)
    :param num2_cmty: 社区编号(1,2,3,4,5)
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
    print(
        f"第{layer1}层的第{num1_cmty}社区与第{layer2}层的第{num2_cmty}社区连接的边数量为{count},占交叉边总数百分比为{cro_persent}"
    )

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

        print(
            f"第{layer1}层的第{num1_cmty}社区内部总边为{count_layer1},占本层边总数的{layer1_perinner}\n"
            f"第{layer2}层的第{num2_cmty}社区内部总边为{count_layer2},占本层边总数的{layer2_perinner}"
        )
    return count,cro_persent



# 不同层，同编号社区连接
print('不同层，同编号社区连接:')
static_cm(1, 2, 1, 1, Cmty, Cross)
print('-------------')
static_cm(1, 2, 2, 2, Cmty, Cross)
print('-------------')
static_cm(1, 2, 3, 3, Cmty, Cross)
print('-------------')
static_cm(1, 2, 4, 4, Cmty, Cross)
print('-------------')
static_cm(1, 2, 5, 5, Cmty, Cross)
print('-------------')
static_cm(0, 3, 2, 2, Cmty, Cross)
print('-------------')
static_cm(0, 4, 1, 1, Cmty, Cross)
print('-------------')
static_cm(1, 4, 2, 2, Cmty, Cross)
print('-------------')
static_cm(2, 4, 2, 2, Cmty, Cross, inter=True)

# 不同层，不同编号社区连接
print("不同层，不同编号社区连接:")
static_cm(1, 2, 1, 2, Cmty, Cross)
print('-------------')
static_cm(2, 3, 2, 3, Cmty, Cross)
print('-------------')
static_cm(3, 4, 3, 4, Cmty, Cross)
print('-------------')
static_cm(1, 4, 2, 1, Cmty, Cross)
print('-------------')
static_cm(2, 4, 4, 2, Cmty, Cross, inter=True)




