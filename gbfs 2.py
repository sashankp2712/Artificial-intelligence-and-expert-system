import heapq

# Heuristic values (assumed smaller near goal)
h = {
    'A': 10,
    'M': 8,
    'P': 7,
    'L': 6,
    'U': 5,
    'C': 4,
    'R': 3,
    'N': 4,
    'S': 2,
    'F': 0
}

graph = {
    'A': ['M', 'P'],
    'M': ['L', 'U', 'C'],
    'P': ['C', 'R'],
    'L': ['N'],
    'U': ['N', 'S', 'F', 'C'],
    'C': ['R'],
    'R': ['F'],
    'N': ['S'],
    'S': ['F'],
    'F': []
}

def gbfs(start, goal):
    visited = set()
    queue = []
    heapq.heappush(queue, (h[start], start))

    print("Image 2 GBFS Path:")

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

gbfs('A', 'F')
