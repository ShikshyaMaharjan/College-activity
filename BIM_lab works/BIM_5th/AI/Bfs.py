def bfs(graph, start):

    visited = set()        # create empty visited set
    queue = [start]        # create queue
    visited.add(start)     # add start node to visited

    while queue:

        node = queue.pop(0)      # remove first element
        print(node, end=" ")     # print node

        if node not in graph:
            continue

        for neighbour in graph[node]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# create graph
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):

    node = input("Enter node: ")
    neighbours = input("Enter neighbours (space separated): ").split()

    graph[node] = neighbours


start = input("Enter starting node: ")

print("BFS Traversal:")

bfs(graph, start)