import math

# Tree structure
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [2, 3],
    'E': [5, 9],
    'F': [0, 1],
    'G': [7, 5]
}

# Max and Min nodes
max_nodes = ['A', 'D', 'E', 'F', 'G']
min_nodes = ['B', 'C']

def alphabeta(node, alpha, beta):
    
    # If terminal node (leaf values list)
    if isinstance(tree[node][0], int):
        if node in max_nodes:
            value = max(tree[node])
        else:
            value = min(tree[node])
        print(f"Node {node} value:", value)
        return value

    # MAX node
    if node in max_nodes:
        value = -math.inf

        for child in tree[node]:
            value = max(value, alphabeta(child, alpha, beta))
            alpha = max(alpha, value)

            # Pruning condition
            if beta <= alpha:
                print(f"Pruned at node {child}")
                break

        return value

    # MIN node
    elif node in min_nodes:
        value = math.inf

        for child in tree[node]:
            value = min(value, alphabeta(child, alpha, beta))
            beta = min(beta, value)

            # Pruning condition
            if beta <= alpha:
                print(f"Pruned at node {child}")
                break

        return value


# Run from root
result = alphabeta('A', -math.inf, math.inf)
print("\nOptimal value at root (A):", result)