edges = [[1,2],
[2,4],
[2,5],
[1,6],
[6,9],
[6,10],
[1,3],
[3,7],
[3,8]]
import collections
def BFS(edges, start, end):
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    queue = []
    visited = [False]*(len(graph)+1)
    visited[start] = True
    #print visited
    queue.append(start)
    parents = graph.keys()
    print(parents)
    while queue:
        #print queue, graph
        current = queue.pop(0)
        for neighbor in graph[current]:
            if visited[neighbor] is False:
                print(neighbor)
                visited[neighbor] = True
                parents[neighbor-1] = current
                queue.append(neighbor)
    print(parents)
    i = end
    hops = 0
    while start != i:
        print(start, i, parents[i-1])
        hops += 1
        i = parents[i-1]
    print(hops +1)
    #print graph


graph = collections.defaultdict(list)
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
stack = []
visited = [False]*(len(graph)+1)

parents = graph.keys()
def DFS(edges, start, visited):
    global graph
    global parents
    visited[start] = True
    for i in graph[start]:
        if visited[i] is False:
            print(i)
            parents[i-1] = start
            DFS(edges, i, visited)
    print(parents)

DFS(edges, 2, visited)
#BFS(edges, 6, 8)