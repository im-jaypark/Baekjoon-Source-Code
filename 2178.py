n, m = map(int, input().split())
maze = [input() for i in range(n)]
path = [[(0, 0)]]

while (n - 1, m - 1) not in path[-1]:
    path.append([])
    for i in path[-2]:
        for j in range(-1, 2, 2):
            if 0 in i and j == -1:
                continue
            try:
                if maze[i[0]][i[1] + j] == "1":
                    if (i[0], i[1] + j) not in path[-1]:
                        if len(path) < 4 or (i[0], i[1] + j) not in path[-3]:
                            path[-1].append((i[0], i[1] + j))
            except:
                pass

            try:
                if maze[i[0] + j][i[1]] == "1":
                    if (i[0] + j, i[1]) not in path[-1]:
                        if len(path) < 4 or (i[0] + j, i[1]) not in path[-3]:
                            path[-1].append((i[0] + j, i[1]))
            except:
                pass

print(len(path))
