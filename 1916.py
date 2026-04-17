from heapq import *

N = int(input())
M = int(input())
graph = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
dists = [float("inf")] * (N + 1)
distQueue = []

for i in range(M):
    s, e, cost = map(int, input().split())
    graph[s].append([e, cost])

start, end = map(int, input().split())
dists[start] = 0
heappush(distQueue, [0, start])

while distQueue:
    currentCity = heappop(distQueue)[1]
    visited[currentCity] = True

    if currentCity == end:
        break

    for road in graph[currentCity]:
        if not visited[road[0]]:
            if dists[currentCity] + road[1] < dists[road[0]]:
                dists[road[0]] = dists[currentCity] + road[1]
                heappush(distQueue, [dists[road[0]], road[0]])

print(dists[end])
