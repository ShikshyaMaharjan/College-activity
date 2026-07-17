graph = {
    'A': [('B',1), ('C',4)],
    'B': [('D',2), ('E',5)],
    'C': [('F',1)],
    'D': [('G',3)],
    'E': [('G',2)],
    'F': [('G',5)],
    'G': []
}

h = {
    'A':7,
    'B':6,
    'C':4,
    'D':3,
    'E':2,
    'F':4,
    'G':0
}

open_list = [('A', 0)]
visited = {}
parent = {'A': None}

goal = 'G'

while open_list:
    open_list.sort(key=lambda x: x[1] + h[x[0]])
    node, cost = open_list.pop(0)

    if node == goal:
        break

    visited[node] = cost

    for n, c in graph[node]:
        if n not in visited:
            open_list.append((n, cost + c))
            parent[n] = node

path = []
node = goal
while node:
    path.append(node)
    node = parent[node]

path.reverse()

print("Path Found:", path)
print("Total Cost:", cost)