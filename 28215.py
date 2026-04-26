from itertools import *

N, K = map(int, input().split())
houses = [list(map(int, input().split())) for i in range(N)]
bestMaxDist = float("inf")

for comb in list(combinations(list(range(N)), K)):
    maxDist = 0

    for house in houses:
        minDist = float("inf")
        for i in comb:
            shelt = houses[i]
            dist = abs(house[0] - shelt[0]) + abs(house[1] - shelt[1])
            minDist = min(minDist, dist)

        maxDist = max(maxDist, minDist)

    bestMaxDist = min(bestMaxDist, maxDist)

print(bestMaxDist)
