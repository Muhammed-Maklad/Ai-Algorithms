
import heapq

def ucs(graph, start, goal):
    heap = [(0, start, [])]
    visited = set()
    
    while heap:
        (cost, node, path) = heapq.heappop(heap)
        
        if node not in visited:
            visited.add(node)
            path = path + [node]
            
            if node == goal:
                return path
            
            for neighbor, neighbor_cost in graph.get(node, {}).items():
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + neighbor_cost, neighbor, path))
    
    return None

graph = {
    'A': {'B': 1, 'C': 5},
    'B': {'D': 2, 'E': 3},
    'C': {'F': 4},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

solution = ucs(graph, 'A', 'F')
print(solution)
