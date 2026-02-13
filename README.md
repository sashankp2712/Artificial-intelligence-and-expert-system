# Artificial-intelligence-and-expert-system
1) BFS Pseudocode
Algorithm: BFS

Input: Graph G, Start node = 1

1. Create an empty Queue Q
2. Create an empty set Visited
3. Enqueue start node into Q
4. Mark start as Visited

5. While Q is not empty do
      a. Remove node N from front of Q
      b. Print N
      c. For each neighbor M of N in Graph
            If M is not in Visited then
                 Add M to Visited
                 Enqueue M into Q
6. End While

End

2) DFS Pseudocode
Algorithm: DFS_Image1

Input: Graph G, Start node = 1

1. Create an empty set Visited

2. Function DFS(N)
      a. Mark N as Visited
      b. Print N
      c. For each neighbor M of N
            If M is not Visited then
                  Call DFS(M)

3. Call DFS(1)

End
3) BFS Pseudocode

Algorithm: BFS_Image2

Input: Graph G, Start node = 1

1. Create Queue Q
2. Create Visited set
3. Enqueue start node (1)
4. Mark 1 as Visited

5. While Q is not empty do
      a. Dequeue node N
      b. Print N
      c. For each neighbor M of N
            If M not in Visited then
                  Mark M as Visited
                  Enqueue M
6. End While

End

4) DFS Pseudocode

Algorithm: DFS_Image2

Input: Graph G, Start node = 1

1. Create empty Visited set

2. Function DFS(N)
      a. Mark N as Visited
      b. Print N
      c. For each neighbor M of N
            If M not visited then
                  DFS(M)

3. Call DFS(1)

End

5) Uniform Cost Search (UCS)
Algorithm: UCS_Search

Input: Graph G, Start node S, Goal node G

1. Create a Priority Queue PQ
2. Insert (cost=0, S) into PQ
3. Create Visited set

4. While PQ is not empty do
      a. Remove node N with lowest cost
      b. If N is Goal then
            Print "Goal reached"
            Stop
      c. If N not in Visited then
            Add N to Visited
            For each neighbor M of N
                  NewCost = Cost(N) + EdgeCost(N,M)
                  Insert (NewCost, M) into PQ
5. End While

End
6) Greedy Best First Search (GBFS)
Algorithm: GBFS_Search

Input: Graph G, Start node S, Goal node G, Heuristic h(n)

1. Create Priority Queue PQ
2. Insert (h(S), S)
3. Create Visited set

4. While PQ is not empty do
      a. Remove node N with lowest heuristic value
      b. Print N
      c. If N is Goal then
            Print "Goal reached"
            Stop
      d. Mark N as Visited
      e. For each neighbor M of N
            If M not visited then
                  Insert (h(M), M) into PQ
5. End While

End
7) A* Search
Algorithm: Astar_Search

Input: Graph G, Start node S, Goal node G
       g(n) = path cost
       h(n) = heuristic

1. Create Priority Queue PQ
2. Insert (f(S)=g(S)+h(S), S)
3. Set g(S) = 0
4. Create Visited set

5. While PQ is not empty do
      a. Remove node N with lowest f(n)
      b. If N is Goal then
            Print "Goal reached"
            Stop
      c. Mark N as Visited
      d. For each neighbor M of N
            g(M) = g(N) + cost(N,M)
            f(M) = g(M) + h(M)
            Insert (f(M), M) into PQ
6. End While

End
8) Water Jug 
Algorithm: WaterJug_BFS

Input: Capacity (5,3), Start (0,0), Goal = 4

1. Create Queue Q
2. Create Visited set
3. Enqueue (0,0)

4. While Q not empty do
      a. Remove state (x,y)
      b. If x=4 or y=4 then
            Print "Goal reached"
            Stop

      c. Generate all possible states:
            Fill Jug1
            Fill Jug2
            Empty Jug1
            Empty Jug2
            Pour Jug1 -> Jug2
            Pour Jug2 -> Jug1

      d. Add new states to Q if not visited
5. End While

End
9) Water Jug (3 Containers: 8L, 5L, 3L)
Algorithm: ThreeJug_BFS

Input: Capacity (8,5,3)
Start = (8,0,0)
Goal = (4,4,0)

1. Create Queue Q
2. Create Visited set
3. Enqueue Start

4. While Q not empty do
      a. Remove state (A,B,C)
      b. If state = Goal then
            Print "Goal reached"
            Stop

      c. For each pair of jugs (i → j)
            Pour water from i to j
            Generate new state

      d. If new state not visited
            Add to Q
5. End While

End
10)Minimax

Algorithm: Minimax(node, depth, isMax)

Input: Game tree node

1. If node is terminal then
      return value(node)

2. If isMax = TRUE then
      best = -∞
      For each child C of node
            val = Minimax(C, depth+1, FALSE)
            best = max(best, val)
      return best

3. Else (Min node)
      best = +∞
      For each child C of node
            val = Minimax(C, depth+1, TRUE)
            best = min(best, val)
      return best

