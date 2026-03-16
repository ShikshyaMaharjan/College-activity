import heapq

def astar_search(graph, h, start, goal):

    # priority queue storing (f(n), node)
    pq = []
    heapq.heappush(pq, (0, start))

    g = {start: 0}
    parent = {start: None}

    while pq:
        f_value, node = heapq.heappop(pq)
        print("Visiting:", node, "f(n):", f_value)

        if node == goal:
            # construct path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()
            return path

        for child, weight in graph.get(node, []):
            new_cost = g[node] + weight

            if child not in g or new_cost < g[child]:
                g[child] = new_cost
                f = new_cost + h[child]

                heapq.heappush(pq, (f, child))
                parent[child] = node

    return None


# Example Weighted Graph
graph = {
    'S': [('A', 2), ('B', 4)],
    'A': [('C', 3), ('D', 1)],
    'B': [('E', 5)],
    'C': [],
    'D': [('G', 2)],
    'E': [],
    'G': []
}

# Heuristic values
heuristic = {
    'S': 7,
    'A': 5,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'G': 0
}

start = 'S'
goal = 'G'

result = astar_search(graph, heuristic, start, goal)

if result:
    print("\nOptimal Path:", " -> ".join(result))
else:
    print("Goal cannot be reached.")