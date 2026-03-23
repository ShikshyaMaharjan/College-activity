import math

# Define the tree as a dictionary
# Each node points to its children
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    # Terminal nodes
    'H': -1, 'I': 4, 'J': 2, 'K': 6,
    'L': -3, 'M': -5, 'N': 0, 'O': 7
}

# Define which nodes are Max or Min
max_nodes = ['A', 'D', 'E', 'F', 'G']   # Max nodes
min_nodes = ['B', 'C']                   # Min nodes

# Minimax function
def minimax(node):
    # If terminal node, return its value
    if node not in tree or not isinstance(tree[node], list):
        return tree[node]
    
    children = tree[node]
    
    if node in max_nodes:
        return max(minimax(child) for child in children)
    elif node in min_nodes:
        return min(minimax(child) for child in children)

# Run Minimax from root
best_value = minimax('A')
print("Minimax value at root (A):", best_value)