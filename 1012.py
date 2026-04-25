import sys
sys.setrecursionlimit(10000)

def search(row, column):
    farm[row][column] = 0

    if row != 0 and farm[row - 1][column] == 1:
        search(row - 1, column)
    if row != n - 1 and farm[row + 1][column] == 1:
        search(row + 1, column)

    if column != 0 and farm[row][column - 1] == 1:
        search(row, column - 1)
    if column != m - 1 and farm[row][column + 1] == 1:
        search(row, column + 1)

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    farm = [[0 for l in range(m)] for j in range(n)]
    groups = 0

    for j in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for j in range(n):
        for l in range(m):
            if farm[j][l] == 1:
                groups += 1
                search(j, l)

    print(groups)
