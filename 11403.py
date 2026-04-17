import sys
sys.setrecursionlimit(10 ** 4)

def search(row, start):
    for i in range(n):
        if paths[row][i] and not visits[row][i]:
                visits[row][i] = 1
                possibles[start][i] = 1
                search(i, start)

n = int(input())
paths = [list(map(int, input().split())) for i in range(n)]
possibles = [[0] * n for i in range(n)]

for i in range(n):
    visits = [[0] * n for i in range(n)]
    search(i, i)

for i in possibles:
    print(*i)
