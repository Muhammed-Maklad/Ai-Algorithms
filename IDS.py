def ids(graph, start, goal, max_depth):
    for depth in range(max_depth):
        visited = []
        path = dfs(graph, start, goal, visited, depth)
        if path:
            return path
    return None

def dfs(graph, node, goal, visited, max_depth):
    if node in visited or max_depth < 0:
        return None
    visited.append(node)
    if node == goal:
        return [node]
    for neighbor in graph.get(node, []):
        path = dfs(graph, neighbor, goal, visited, max_depth - 1)
        if path:
            return [node] + path
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

max_depth = 3
solution = ids(graph, 'A', 'F', max_depth)
print(solution)
