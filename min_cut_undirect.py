import networkx as nx
import matplotlib.pyplot as plt

def stoer_wagner(graph):
    n = len(graph)  # 图中节点的数量
    min_cut_capacity = float('inf')

    # 初始化标记数组
    is_in_a = [False] * n

    for phase in range(n - 1):
        # 选择“A”集合中的一个节点
        a_node = -1
        for i in range(n):
            if not is_in_a[i]:
                a_node = i
                break

        # 找到最小割边
        cut_capacity = min_cut(graph, is_in_a, a_node)
        min_cut_capacity = min(min_cut_capacity, cut_capacity)

        # 合并节点
        merge_nodes(graph, is_in_a, a_node)

    return min_cut_capacity

def min_cut(graph, is_in_a, a_node):
    n = len(graph)
    min_cut_capacity = float('inf')

    while True:
        max_edge_weight = -1
        b_node = -1

        # 找到最大权重的边（最小割边）
        for i in range(n):
            if not is_in_a[i]:
                for j in range(n):
                    if is_in_a[j]:
                        if graph[i][j] > max_edge_weight:
                            max_edge_weight = graph[i][j]
                            a_node = i
                            b_node = j

        if max_edge_weight == -1:
            return min_cut_capacity

        min_cut_capacity = max_edge_weight
        is_in_a[a_node] = True

    return min_cut_capacity

def merge_nodes(graph, is_in_a, a_node):
    n = len(graph)

    # 合并节点
    for i in range(n):
        if not is_in_a[i]:
            graph[a_node][i] += graph[i][a_node]
            graph[i][a_node] = graph[a_node][i]

    is_in_a[a_node] = True

def visualize_stoer_wagner(graph, min_cut_set, cut_capacity):
    # 创建 NetworkX 图
    G = nx.Graph()
    for i in range(len(graph)):
        G.add_node(i)
        for j in range(i+1, len(graph)):
            G.add_edge(i, j, weight=graph[i][j])

    # 绘制图
    pos = nx.spring_layout(G, seed=42)
    labels = {i: str(i) for i in range(len(graph))}

    # 绘制节点
    nx.draw_networkx_nodes(G, pos)
    # 绘制边
    nx.draw_networkx_edges(G, pos)
    # 绘制标签
    nx.draw_networkx_labels(G, pos, labels=labels)

    # 绘制最小割边
    min_cut_edges = [(i, j) for i in range(len(graph)) for j in range(i+1, len(graph)) if (i in min_cut_set) != (j in min_cut_set)]
    nx.draw_networkx_edges(G, pos, edgelist=min_cut_edges, edge_color='r', width=2)

    plt.title(f"Min Cut Capacity: {cut_capacity}")
    plt.show()

# 示例用法
graph = [
    [0, 10, 20, 30],
    [10, 0, 5, 0],
    [20, 5, 0, 15],
    [30, 0, 15, 0]
]

is_in_a = [False] * len(graph)
min_cut_capacity = stoer_wagner(graph)
min_cut_set = [i for i, in_a in enumerate(is_in_a) if in_a]

visualize_stoer_wagner(graph, min_cut_set, min_cut_capacity)
