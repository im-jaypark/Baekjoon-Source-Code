n, m = map(int, input().split())
square = [[0] * n for i in range(n)]

for i in range(n):
    row = list(map(int, input().split()))

    for j in range(n):
        if j == 0:
            square[i][j] = row[j]
        else:
            square[i][j] = row[j] + square[i][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0

    for j in range(x1 - 1, x2):
        if y1 == 1:
            total += square[j][y2 - 1]
        else:
            total += square[j][y2 - 1] - square[j][y1 - 2]

    print(total)
