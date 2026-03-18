def depth_limited_search(graph, current, goal, depth_limit, level=0):

    print("Visiting:", current, "Level:", level)

    # Check if goal node is reached
    if current == goal:
        return True

    # Stop searching if depth limit reached
    if level == depth_limit:
        return False

    # Explore child nodes
    for next_node in graph.get(current, []):
        if depth_limited_search(graph, next_node, goal, depth_limit, level + 1):
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

start = 'S'
goal = 'G'
limit = 3

result = depth_limited_search(graph, start, goal, limit)

if result:
    print("Goal node found within the depth limit.")
else:
    print("Goal node not found within the given depth limit.")