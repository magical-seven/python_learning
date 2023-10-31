import networkx as nx
import matplotlib.pyplot as plt


def ford_fulkerson(graph, source, sink):
    # 初始化流量为0
    for u, v, attr in graph.edges(data=True):
        attr['flow'] = 0

    # 寻找增广路径
    def find_augmenting_path(graph, source, sink):
        visited = set()
        stack = [(source, [source])]
        while stack:
            node, path = stack.pop()
            visited.add(node)
            for neighbor, attr in graph[node].items():
                if neighbor not in visited and attr['capacity'] > attr['flow']:
                    new_path = path + [neighbor]
                    if neighbor == sink:
                        return new_path
                    stack.append((neighbor, new_path))
        return None

    # 主循环：寻找增广路径并更新流量
    augmenting_path = find_augmenting_path(graph, source, sink)
    while augmenting_path:
        # 寻找路径上的最小剩余容量
        min_capacity = min(
            graph[u][v]['capacity'] - graph[u][v]['flow'] for u, v in zip(augmenting_path, augmenting_path[1:]))

        # 更新路径上的边的流量
        for u, v in zip(augmenting_path, augmenting_path[1:]):
            graph[u][v]['flow'] += min_capacity
            graph[v][u]['flow'] -= min_capacity  # 反向边

        augmenting_path = find_augmenting_path(graph, source, sink)

    # 计算最小割的容量
    min_cut_capacity = sum(graph[source][v]['capacity'] for v in graph[source]) - sum(
        graph[source][v]['capacity'] - graph[source][v]['flow'] for v in graph[source])

    # 可视化最小割结果
    visualize_min_cut(graph, source, sink)

    return min_cut_capacity


def visualize_min_cut(graph, source, sink):
    # 根据最小割算法的结果，标记图中的节点，将其分为两个部分
    min_cut_nodes = set()
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited and graph[node][neighbor]['capacity'] - graph[node][neighbor]['flow'] > 0:
                min_cut_nodes.add(neighbor)
                dfs(neighbor)

    dfs(source)

    # 绘制图形
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(10, 6))
    node_colors = ['lightblue' if node in min_cut_nodes else 'lightcoral' for node in graph.nodes]
    edge_labels = {(u, v): f'{graph[u][v]["flow"]} / {graph[u][v]["capacity"]}' for u, v in graph.edges}
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_labels(graph, pos, font_size=10)
    nx.draw_networkx_edges(graph, pos, alpha=0.7)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Minimum Cut Visualization")
    plt.axis('off')
    plt.show()



# 创建一个有向图
G = nx.DiGraph()

# 添加节点和边，以及边的容量
nodes = ['S', 'A', 'B', 'C', 'D', 'T']
edges = [('S', 'A', 4), ('S', 'B', 2),
         ('A', 'B', 3), ('A', 'C', 2),
         ('B', 'C', 5), ('B', 'D', 2),
         ('C', 'T', 3), ('D', 'T', 4)]

G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges, weight='capacity')



# 指定源节点和汇节点
source = 'S'
sink = 'T'

# 调用Ford-Fulkerson算法求解最小割
min_cut = ford_fulkerson(G, source, sink)

# 打印最小割的容量
print("最小割的容量为:", min_cut)
