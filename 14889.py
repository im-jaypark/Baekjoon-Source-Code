from itertools import *

N = int(input())
stats = [list(map(int, input().split())) for i in range(N)]
minDiff = float("inf")

for team in list(combinations(list(range(N)), N // 2)):
    opp = [j for j in range(N) if j not in team]
    diff = 0

    for x in range(N // 2):
        for y in range(N // 2):
            if x != y:
                diff += stats[team[x]][team[y]]
                diff -= stats[opp[x]][opp[y]]

    minDiff = min(abs(diff), minDiff)

print(minDiff)
