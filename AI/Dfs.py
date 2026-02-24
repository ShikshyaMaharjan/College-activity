def dfs(graph, start, visited):

    print(start, end=" ")      # print node

    visited.add(start)         # mark as visited

    for neighbour in graph[start]:

        if neighbour not in visited:

            dfs(graph, neighbour, visited)


# create graph
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):

    node = input("Enter node: ")

    neighbours = input("Enter neighbours (space separated): ").split()

    graph[node] = neighbours


start = input("Enter starting node: ")

visited = set()

print("DFS Traversal:")

dfs(graph, start, visited)