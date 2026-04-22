import sys
sys.setrecursionlimit(10 ** 5)

def dfs(x, y):
    visited[x][y] = 1
    nears = ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))

    for near in nears:
        if 0 <= near[0] < N and 0 <= near[1] < N:
            if city[near[0]][near[1]] > i and visited[near[0]][near[1]] == 0:
                dfs(near[0], near[1])

N = int(input())
city = [list(map(int, input().split())) for i in range(N)]
maxHeight = max([max(i) for i in city])
maxAreas = 0

for i in range(maxHeight):
    visited = [[0] * N for j in range(N)]
    areas = 0

    for j in range(N):
        for k in range(N):
            if city[j][k] > i and visited[j][k] == 0:
                dfs(j, k)
                areas += 1

    maxAreas = max(maxAreas, areas)

print(maxAreas)
