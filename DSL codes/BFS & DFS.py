# Adjacency List for BFS
adj_list = {
    'A': ['B', 'D'],
    'B': ['D', 'E','C'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Adjacency Matrix for DFS
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
index = {node: i for i, node in enumerate(nodes)}
adj_matrix = [
    # A  B  C  D  E  F
    [0, 1, 1, 0, 0, 0],  # A
    [0, 0, 0, 0, 1, 0],  # B
    [0, 0, 0, 0, 0, 1],  # C
    [0, 0, 0, 0, 0, 0],  # D
    [0, 0, 0, 0, 0, 1],  # E
    [0, 0, 0, 0, 0, 0]   # F
]

def bfs(start):
    visited = set()
    queue = [start]
    result = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(adj_list[node])
    return result

def dfs(start):
    visited = set()
    result = []

    def dfs_recursive(node):
        visited.add(node)
        result.append(node)
        i = index[node]
        for j, connected in enumerate(adj_matrix[i]):
            if connected and nodes[j] not in visited:
                dfs_recursive(nodes[j])

    dfs_recursive(start)
    return result

# Run traversals
print("BFS Traversal from A:", bfs('A'))
print("DFS Traversal from A:", dfs('A'))