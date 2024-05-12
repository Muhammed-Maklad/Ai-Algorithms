def bfs(graph, start, goal):
    visited = [] 
    queue = [[start]]
    while queue:
        path = queue.pop(0)    
        node = path[-1]
        if node in visited: 
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent = graph.get(node, [])
            for neighbor in adjacent:
                new_path = list(path) 
                new_path.append(neighbor)
                queue.append(new_path) 

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

solution = bfs(graph, 'A', 'F')
print(solution)
