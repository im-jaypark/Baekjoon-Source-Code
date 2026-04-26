n, m = map(int, input().split())
minPaints = 32
board = []

for i in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        repaints = [0, 0]
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] == "B":
                        repaints[0] += 1
                    else:
                        repaints[1] += 1
                else:
                    if board[k][l] == "B":
                        repaints[1] += 1
                    else:
                        repaints[0] += 1
        minPaints = min(minPaints, min(repaints))

print(minPaints)
