import heapq

# Heuristic values
h = {
    'A': 40,
    'B': 32,
    'C': 30,
    'D': 35,
    'E1': 17,
    'E2': 19,
    'H': 10,
    'G': 0
}

# Graph structure
graph = {
    'A': ['D', 'C', 'B'],
    'D': ['E1'],
    'C': ['E1', 'E2'],
    'B': ['E2'],
    'E1': ['G'],
    'E2': ['H'],
    'H': ['G'],
    'G': []
}

def gbfs(start, goal):
    visited = set()
    queue = []
    heapq.heappush(queue, (h[start], start))

    print("Image 1 GBFS Path:")

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

gbfs('A', 'G')
