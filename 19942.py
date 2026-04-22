from itertools import *

N = int(input())
minimums = list(map(int, input().split()))
table = [list(map(int, input().split())) for i in range(N)]
minCost = float("inf")
combi = []

for i in list(product(list(range(2)), repeat=N)):
    total = [0] * 5
    tempCombi = []
    valid = True

    for item in range(N):
        if i[item] == 1:
            tempCombi.append(item + 1)
            
            for j in range(5):
                total[j] += table[item][j]

    for j in range(4):
        if total[j] < minimums[j]:
            valid = False
            break

    if valid:
        if total[4] < minCost:
            minCost = total[4]
            combi = tempCombi.copy()
        elif total[4] == minCost:
            combi = min(combi, tempCombi.copy())

if minCost != float("inf"):
    print(minCost)
    print(*combi)
else:
    print(-1)
