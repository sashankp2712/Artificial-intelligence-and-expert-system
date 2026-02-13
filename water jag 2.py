from collections import deque

# Capacities
cap = (8, 5, 3)

# Initial and Goal
start = (8, 0, 0)
goal = (4, 4, 0)

def pour(state, i, j):
    state = list(state)
    amount = min(state[i], cap[j] - state[j])
    state[i] -= amount
    state[j] += amount
    return tuple(state)

def bfs():
    visited = set()
    queue = deque()
    
    queue.append(start)
    visited.add(start)
    
    print("Steps:")
    
    while queue:
        state = queue.popleft()
        print(state)
        
        if state == goal:
            print("Goal reached!")
            return
        
        # Generate all possible pours
        for i in range(3):
            for j in range(3):
                if i != j:
                    new_state = pour(state, i, j)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append(new_state)

bfs()
