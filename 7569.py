from collections import deque
import sys
input = sys.stdin.readline

def ripen(x, y, z):
    global nextTomatoes
    global changed
    global zeros

    moves = ((-1, 0, 0), (1, 0, 0), (0, -1, 0),
             (0, 1, 0), (0, 0, -1), (0, 0, 1))

    posVars = (x, y, z)
    edges = (h, n, m)

    for i in range(3):
        for j in range(2):
            dx, dy, dz = moves[2 * i + j]
            dx += x; dy += y; dz += z

            if posVars[i] != j * (edges[i] - 1) and farm[dx][dy][dz] == 0:
                farm[dx][dy][dz] = 1
                deque.append(nextTomatoes, [dx, dy, dz])
                zeros -= 1

m, n, h = map(int, input().split())
farm = [[list(map(int, input().split())) for j in range(n)] for i in range(h)]
zeros = 0
days = 0
nextTomatoes = deque()

for i in range(h):
    for j in range(n):
        zeros += farm[i][j].count(0)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if farm[i][j][k] == 1:
                deque.append(nextTomatoes, [i, j, k])

while nextTomatoes:
    days += 1
    ripeTomatoes = nextTomatoes
    nextTomatoes = deque()

    for i in ripeTomatoes:
        ripen(*i)

if not zeros:
    print(days - 1)
else:
    print(-1)
