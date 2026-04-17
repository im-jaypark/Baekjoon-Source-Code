from collections import deque
import sys

input = sys.stdin.readline

def search(x, y):
    global nextSearch
    
    posVars = (x, x, y, y)
    edges = (0, n - 1, 0, m - 1)
    coords = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for i in range(4):
        dx, dy = x + coords[i][0], y + coords[i][1]

        if posVars[i] != edges[i] and land[dx][dy] == -1:
            deque.append(nextSearch, (dx, dy))
            land[dx][dy] = time

n, m = map(int, input().split())
land = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if land[i][j] == 1:
            land[i][j] = -1
        elif land[i][j] == 2:
            start = (i, j)
            land[i][j] = 0

nextSearch = deque([start])
time = 0

while nextSearch:
    time += 1
    searchNow = nextSearch
    nextSearch = deque()

    for i in searchNow:
        search(i[0], i[1])

for i in land:
    print(*i)
