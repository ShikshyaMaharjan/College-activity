# Hill Climbing Algorithm (Simple)

# Graph with heuristic values
graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 1,
    'B': 3,
    'C': 2,
    'D': 4,
    'E': 5,
    'F': 3
}

def hill_climbing(start):
    current = start
    print("Start at:", current)

    while True:
        neighbors = graph[current]

        if not neighbors:
            break

        # Find best neighbor
        next_node = current
        best_value = heuristic[current]

        for node, value in neighbors:
            if value > best_value:
                best_value = value
                next_node = node

        # If no better neighbor, stop
        if next_node == current:
            break

        current = next_node
        print("Move to:", current)

    print("Reached peak:", current)


# Run the algorithm
hill_climbing('A')