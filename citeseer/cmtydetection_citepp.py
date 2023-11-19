import networkx as nx
import community
from linklayer import layer_node,layer_link

"""
# 节点以及连接列表
layer_node = [layer0_node, layer1_node, layer2_node]
layer_link = [layer0_link, layer1_link, layer2_link]
"""

# 创建图
G = nx.Graph()
# 添加节点和边，这里使用示例数据，具体根据您的网络结构添加节点和边
G.add_edges_from(layer_link[1])

# 使用Louvain算法进行社区检测，设置resolution参数
communities = community.best_partition(G, resolution=1.0)

# 输出社区的数量
num_communities = len(set(communities.values()))
print(f"Number of communities: {num_communities}")








def savecmty(
        outpathf:str,
        communities:dict)->None:
    # 将社区信息输出到.txt文件
    with open(outpathf, 'w') as file:
        for node, community_id in communities.items():
            file.write(f"{node}\t{community_id}\n")
    print(f"Community information has been written to {outpathf}")


'''
# 将社区信息输出到.txt文件
output_file = 'test1.txt'
with open(output_file, 'w') as file:
    for node, community_id in communities.items():
        file.write(f"{node}\t{community_id}\n")

print(f"Community information has been written to {output_file}")
'''