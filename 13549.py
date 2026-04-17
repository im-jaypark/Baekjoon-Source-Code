from heapq import *

n, k = map(int, input().split())
upperbound = max(n, k) + abs(n - k)
dists = [float("inf")] * (upperbound + 1)
dists[n] = 0
distQueue = [[0, n]]
visited = [False] * (upperbound + 1)

while distQueue:
    pos = heappop(distQueue)[1]
    
    if visited[pos]:
        continue
    if pos == k:
        break
    
    visited[pos] = True
    
    for next in [pos + 1, pos - 1, 2 * pos]:
        if 0 <= next <= upperbound:
            if next == 2 * pos:
                added = 0
            else:
                added = 1
            
            if dists[pos] + added < dists[next]:
                dists[next] = dists[pos] + added
                heappush(distQueue, [dists[next], next])

print(dists[k])
