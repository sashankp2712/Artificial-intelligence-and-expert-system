import heapq

# Heuristic values
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

# Graph with edge costs
graph = {
    'S': [('A', 3), ('D', 4)],
    'A': [('B', 4), ('D', 5)],
    'D': [('E', 2)],
    'E': [('F', 4), ('B', 5)],
    'B': [('C', 4)],
    'C': [],
    'F': [('G', 3.5)],
    'G': []
}

def astar(start, goal):
    queue = []
    heapq.heappush(queue, (h[start], 0, start))
    visited = set()

    print("Image 1 A* Path:")

    while queue:
        f, g, node = heapq.heappop(queue)

        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == goal:
            print("\nGoal Reached with cost:", g)
            return

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                heapq.heappush(queue, (new_f, new_g, neighbor))

astar('S', 'G')
