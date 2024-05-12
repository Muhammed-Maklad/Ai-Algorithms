def dfs (graph , start, goal,visted=None):
    if visted is None:
        visted=[]
    visted.append(start)

    if start == goal:
        return [start]
    
    for neighbour in graph.get(start,[]):
        if neighbour not in visted:
            path = dfs(graph , neighbour, goal,visted.copy())
            if path:
                return [start]+path
    return None

graph = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F'],
  'D': [],
  'E': ['F'],
  'F': []
}

solution = dfs(graph, 'A', 'F')
print(solution)
