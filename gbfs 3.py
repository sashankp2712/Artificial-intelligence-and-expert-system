import heapq

h = {
    'S': 11.5,
    'A': 10.1,
    'D': 9.2,
    'E': 7.1,
    'B': 5.8,
    'C': 8.4,
    'F': 3.5,
    'G': 0
}

graph = {
    'S': ['A', 'D'],
    'A': ['B', 'C', 'D'],
    'D': ['E'],
    'E': ['F', 'B'],
    'B': ['C'],
    'C': [],
    'F': ['G'],
    'G': []
}

def gbfs(start, goal):
    visited = set()
    queue = []
    heapq.heappush(queue, (h[start], start))

    print("Image 3 GBFS Path:")

    while queue:
        _, node = heapq.heappop(queue)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal Reached")
            return

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (h[neighbor], neighbor))

gbfs('S', 'G')
