from collections import deque

def bfs(walls):
    tempLab = [[lab[i][j] for j in range(M)] for i in range(N)]
    bfsQueue = deque()
    zeroCount = 0

    for wall in walls:
        tempLab[zeros[wall][0]][zeros[wall][1]] = 1

    for i in range(N):
        for j in range(M):
            if tempLab[i][j] == 2:
                deque.append(bfsQueue, (i, j))

    while bfsQueue:
        toCheck = deque.popleft(bfsQueue)

        for i in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newX, newY = toCheck[0] + i[0], toCheck[1] + i[1]

            if 0 <= newX < N and 0 <= newY < M:
                if tempLab[newX][newY] == 0:
                    tempLab[newX][newY] = 2
                    deque.append(bfsQueue, (newX, newY))

    for i in range(N):
        for j in range(M):
            if tempLab[i][j] == 0:
                zeroCount += 1

    return zeroCount

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for i in range(N)]
zeros = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]
zeroCount = len(zeros)
mostSpace = 0

for i in range(zeroCount):
    for j in range(i + 1, zeroCount):
        for k in range(j + 1, zeroCount):
            mostSpace = max(bfs((i, j, k)), mostSpace)

print(mostSpace)
