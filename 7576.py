m, n = map(int, input().split())
farm = [list(map(int, input().split())) for i in range(n)]
path = [[]]
days = 0
zeros = 0

for i in range(n):
    for j in range(m):
        if farm[i][j] == 0:
            zeros += 1
        elif farm[i][j] == 1:
            path[0].append([i, j])

while zeros != 0:
    days += 1
    changed = False
    path.append([])

    for i in path[-2]:
        if i[0] != 0 and farm[i[0] - 1][i[1]] == 0:
            path[-1].append([i[0] - 1, i[1]]) 
            farm[i[0] - 1][i[1]] = 1
            zeros -= 1
            changed = True
        if i[0] != n - 1 and farm[i[0] + 1][i[1]] == 0:
            path[-1].append([i[0] + 1, i[1]])
            farm[i[0] + 1][i[1]] = 1
            zeros -= 1
            changed = True
        if i[1] != 0 and farm[i[0]][i[1] - 1] == 0:
            path[-1].append([i[0], i[1] - 1])
            farm[i[0]][i[1] - 1] = 1
            zeros -= 1
            changed = True
        if i[1] != m - 1 and farm[i[0]][i[1] + 1] == 0:
            path[-1].append([i[0], i[1] + 1])
            farm[i[0]][i[1] + 1] = 1
            zeros -= 1
            changed = True

    if zeros == 0:
        break
    elif changed == False:
        days = -1
        break

print(days)
