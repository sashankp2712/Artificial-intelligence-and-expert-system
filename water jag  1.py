from collections import deque

# Jug capacities
max_x = 5
max_y = 3

# Goal
goal = 4

def bfs():
    visited = set()
    queue = deque()
    
    # start state
    queue.append((0, 0))
    visited.add((0, 0))
    
    print("BFS Steps:")
    
    while queue:
        x, y = queue.popleft()
        print((x, y))
        
        # Goal check
        if x == goal or y == goal:
            print("Goal reached!")
            return
        
        # Possible operations
        next_states = [
            (max_x, y),        # Fill 5L
            (x, max_y),        # Fill 3L
            (0, y),            # Empty 5L
            (x, 0),            # Empty 3L
            (x - min(x, max_y - y), y + min(x, max_y - y)),  # Pour 5 -> 3
            (x + min(y, max_x - x), y - min(y, max_x - x))   # Pour 3 -> 5
        ]
        
        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

bfs()
