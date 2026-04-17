from heapq import *

def shortest(start, ends):
    visited = [False] * (N + 1)
    dists = [float("inf")] * (N + 1)
    dists[start] = 0
    distQueue = [[0, start]]
    
    while distQueue:
        current = heappop(distQueue)[1]
        
        if visited[current]:
            continue
        
        visited[current] = True
        
        for edge in graph[current]:
            if dists[current] + edge[1] < dists[edge[0]]:
                dists[edge[0]] = dists[current] + edge[1]
                heappush(distQueue, [dists[edge[0]], edge[0]])
        
    return [dists[i] for i in ends]

N, E = map(int, input().split())
graph = [[] for i in range(N + 1)]
majorDists = []

for i in range(E):
    v1, v2, w = map(int, input().split())
    graph[v1].append([v2, w])
    graph[v2].append([v1, w])

p1, p2 = map(int, input().split())

majorDists.append(shortest(1, [p1, p2]))
majorDists.append(shortest(p1, [p2]))
majorDists.append(shortest(N, [p1, p2]))
pathLen = min(majorDists[0][0] + majorDists[2][1],
              majorDists[0][1] + majorDists[2][0]) + majorDists[1][0]

if pathLen == float("inf"):
    print(-1)
else:
    print(pathLen)
