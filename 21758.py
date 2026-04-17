import sys

input = sys.stdin.readline

N = int(input())
hives = list(map(int, input().split()))
maxes = [0] * 3
pSums = [[], []]

maxes[0] = sum(hives[1:-1]) + max(hives[1:-1])

pSums[0].append(sum(hives[1:-1]))
pSums[1].append(sum(hives[1:-1]))

for i in range(N - 2, 0, -1):
    pSums[0].append(pSums[0][-1] - hives[i] + 2 * hives[i + 1])

for i in range(N - 2):
    pSums[1].append(pSums[1][-1] + 2 * hives[i] - hives[i + 1])

maxes[1], maxes[2] = max(pSums[0][1:]), max(pSums[1][1:])

print(max(maxes))
