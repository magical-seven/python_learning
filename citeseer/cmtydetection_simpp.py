import networkx as nx
import community
from linklayer import layer_node,layer_link,layer2_weight
"""
layer_node = [layer0_node, layer1_node, layer2_node]
layer_link = [layer0_link, layer1_link, layer2_link]
layer2_weight
"""



# 创建图
G = nx.Graph()
# 添加节点和边，这里使用示例数据，具体根据您的网络结构添加节点和边
for link, weight in zip(layer_link[2],layer2_weight):
    G.add_edge(link[0],link[1], weight=weight)
# G.add_edges_from(layer_link[2])


# 使用Louvain算法检测社区
communities = community.best_partition(G, weight='weight')

# 将社区信息输出到.txt文件
output_file = 'test2.txt'
with open(output_file, 'w') as file:
    for node, community_id in communities.items():
        file.write(f"{node}\t{community_id}\n")

print(f"Community information has been written to {output_file}")
