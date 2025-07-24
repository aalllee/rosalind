"""
Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.

"""


from collections import defaultdict, deque
adjacency_list = [[1,2],[2,8],[4,10], [5,9], [6,10], [7,9]]

def dfs(node, graph,visited):
    stack = [node]
    while stack:
        curr = stack.pop()
        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

def count_trees(adjacency_list):
    graph = defaultdict(list)
    nodes = set()

    # Step 1: Build the graph
    for u, v in adjacency_list:
        graph[u].append(v)
        graph[v].append(u)
        nodes.add(u)
        nodes.add(v)

    visited = set()
    tree_count = 0

    for node in nodes:
        if node not in visited:
            visited.add(node)
            dfs(node,graph,visited)
            tree_count += 1

    return tree_count


def add_edges(adjacency_list):
    num_trees = count_trees(adjacency_list)
    return num_trees - 1


print(add_edges(adjacency_list))