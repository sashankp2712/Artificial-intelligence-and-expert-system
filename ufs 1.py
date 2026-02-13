import heapq

# Graph with edge costs (assumed cost = node value difference or given)
graph = {
    'A': [('D', 35), ('C', 30), ('B', 32)],
    'D': [('E1', 17)],
    'C': [('E1', 17), ('E2', 19)],
    'B': [('E2', 19)],
    'E1': [('G', 0)],
    'E2': [('H', 5)],
    'H': [('G', 0)],
    'G': []
}

def uniform_cost_search(start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    visited = set()

    while queue:
        cost, node = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)
        print(node, end=" ")

        if node == goal:
            print("\nGoal reached with cost:", cost)
            return

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor))


print("UCS Traversal:")
uniform_cost_search('A', 'G')
