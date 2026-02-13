# Minimax Tree Structure

# Leaf values
tree = {
    'D': [2, 3],
    'E': [5, 9],
    'F': [0, 1],
    'G': [7, 5]
}

# Function for MAX node
def max_node(values):
    return max(values)

# Function for MIN node
def min_node(values):
    return min(values)

# -------- Level 2 (Max nodes) --------
D_val = max_node(tree['D'])   # max(2,3) = 3
E_val = max_node(tree['E'])   # max(5,9) = 9
F_val = max_node(tree['F'])   # max(0,1) = 1
G_val = max_node(tree['G'])   # max(7,5) = 7

print("D =", D_val)
print("E =", E_val)
print("F =", F_val)
print("G =", G_val)

# -------- Level 1 (Min nodes) --------
B_val = min_node([D_val, E_val])   # min(3,9) = 3
C_val = min_node([F_val, G_val])   # min(1,7) = 1

print("B =", B_val)
print("C =", C_val)

# -------- Root (Max) --------
A_val = max_node([B_val, C_val])   # max(3,1) = 3

print("\nOptimal value at Root A =", A_val)
