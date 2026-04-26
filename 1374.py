from heapq import *

N = int(input())
classes = []
roomEnds = [0]

for i in range(N):
    num, start, end = map(int, input().split())
    classes.append((start, end))

classes.sort()

for i in range(N):
    bestRoom = heappop(roomEnds)

    if classes[i][0] < bestRoom:
        heappush(roomEnds, bestRoom)

    heappush(roomEnds, classes[i][1])

print(len(roomEnds))
