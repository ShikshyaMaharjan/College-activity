graph = {
    'S':['A','B'],
    'A':['C','D'],
    'B':['E'],
    'C':['G'],
    'D':['G'],
    'E':['G'],
    'G':[]
}

h = {
    'S':7,
    'A':5,
    'B':6,
    'C':2,
    'D':1,
    'E':4,
    'G':0
}
start = 'S'
goal = 'G'
visited = []
queue = [start]
parent = {start:None}
while queue:
    queue.sort(key=lambda x:h[x])
    node = queue.pop(0)
    if node not in visited:
        visited.append(node)
    if node == goal:
        break
    for n in graph[node]:
      if n not in visited:
            queue.append(n)
            parent[n] = node
path = []
node = goal
while node:
    path.append(node)
    node = parent[node]
path.reverse()
print("Nodes Visited:", visited)
print("Final Path:", path)