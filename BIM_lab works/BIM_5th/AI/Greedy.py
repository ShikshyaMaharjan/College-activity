import heapq

def greedy_search(graph, h, start, goal):
    
    # priority queue
    queue = []
    heapq.heappush(queue, (h[start], start))

    explored = set()

    while queue:
        value, node = heapq.heappop(queue)
        print("Visiting:", node, "Heuristic:", value)

        if node == goal:
            print("Goal reached!")
            return True

        explored.add(node)

        for child in graph.get(node, []):
            if child not in explored:
                heapq.heappush(queue, (h[child], child))

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

# Heuristic values
heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 5,
    'D': 1,
    'E': 3,
    'G': 0
}

start = 'S'
goal = 'G'

result = greedy_search(graph, heuristic, start, goal)

if not result:
    print("Goal node not found.")