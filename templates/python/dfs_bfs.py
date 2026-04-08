from collections import deque


def dfs_recursive(graph, node, visited):
    visited.add(node)
    for nei in graph.get(node, []):
        if nei not in visited:
            dfs_recursive(graph, nei, visited)


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

    return order
