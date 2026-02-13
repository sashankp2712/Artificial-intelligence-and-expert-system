graph = {
    1: [2, 3],
    2: [5, 6],
    3: [4, 7],
    4: [8],
    5: [],
    6: [],
    7: [],
    8: []
}

def dfs(node, visited=None):
    if visited is None:
        visited = set()
        print("Image 2 DFS Traversal:")

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

dfs(1)
