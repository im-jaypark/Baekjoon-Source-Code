import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

def dfs(x, y, color, animal):
    checked[animal][x][y] = 1

    if animal == 0:
        similarColors = [color]
    else:
        if color in ["R", "G"]:
            similarColors = ["R", "G"]
        else:
            similarColors = ["B"]
    
    if x != 0:
        if painting[x - 1][y] in similarColors and checked[animal][x - 1][y] == 0:
            dfs(x - 1, y, similarColors[0], animal)

    if x != n - 1:
        if painting[x + 1][y] in similarColors and checked[animal][x + 1][y] == 0:
            dfs(x + 1, y, similarColors[0], animal)

    if y != 0:
        if painting[x][y - 1] in similarColors and checked[animal][x][y - 1] == 0:
            dfs(x, y - 1, similarColors[0], animal)

    if y != n - 1:
        if painting[x][y + 1] in similarColors and checked[animal][x][y + 1] == 0:
            dfs(x, y + 1, similarColors[0], animal)

n = int(input())
painting = [input() for i in range(n)]
checked = [[[0] * n for j in range(n)] for i in range(2)]
sections = [0, 0]

for i in range(n):
    for j in range(n):
        for k in range(2):
            if checked[k][i][j] == 0:
                dfs(i, j, painting[i][j], k)
                sections[k] += 1

print(*sections)
