def dls(graph, start, goal, depth_limit, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    if start == goal:
        return [start]

    if depth_limit == 0:
        return None

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            path = dls(graph, neighbor, goal, depth_limit - 1, visited.copy())
            if path:
                return [start] + path
    return None

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

depth_limit = 3
solution = dls(graph, 'A', 'F', depth_limit)
print(solution)
