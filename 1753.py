from heapq import *

V, E = map(int, input().split())
K = int(input())
graph = [[] for i in range(V + 1)]
dists = [float("inf")] * (V + 1)
dists[K] = 0
distQueue = [[0, K]]
visited = [False] * (V + 1)

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    
while distQueue:
    currentNode = heappop(distQueue)[1]

    if visited[currentNode]:
        continue

    visited[currentNode] = True

    for edge in graph[currentNode]:
        if dists[currentNode] + edge[1] < dists[edge[0]]:
            dists[edge[0]] = dists[currentNode] + edge[1]
            heappush(distQueue, [dists[edge[0]], edge[0]])

for i in range(1, V + 1):
    if dists[i] == float("inf"):
        print("INF")
    else:
        print(dists[i])
