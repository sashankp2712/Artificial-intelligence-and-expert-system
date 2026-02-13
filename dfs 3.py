graph = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [5],
    5: []
}

def dfs(node, visited=None):
    if visited is None:
        visited = set()
        print("Image 3 DFS Traversal:")

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

dfs(1)
