# Depth Limited Search function
def depth_limited(graph, current, target, level, limit):
    print("Visiting:", current, "Level:", level)

    # Check goal
    if current == target:
        return True

    # Stop if limit reached
    if level == limit:
        return False

    # Explore neighbours
    for child in graph.get(current, []):
        if depth_limited(graph, child, target, level + 1, limit):
            return True

    return False


# Iterative Deepening Search
def iterative_deepening(graph, start, goal, max_limit):

    for limit in range(max_limit + 1):
        print("\nDepth Limit:", limit)

        if depth_limited(graph, start, goal, 0, limit):
            return True

    return False


# Example Graph
graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': ['G'],
    'E': [],
    'G': []
}

start_node = 'S'
goal_node = 'G'
max_limit = 3

result = iterative_deepening(graph, start_node, goal_node, max_limit)

if result:
    print("\nGoal node found!")
else:
    print("\nGoal node not found.")