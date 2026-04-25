n, m = map(int, input().split())
prefix = [[0, 0, 0] for i in range(n + 1)]

for i in range(1, n + 1):
    cowType = int(input())

    for j in range(3):
        prefix[i][j] = prefix[i - 1][j]
        
    if cowType == 1:
        prefix[i][0] += 1
    elif cowType == 2:
        prefix[i][1] += 1
    else:
        prefix[i][2] += 1

for i in range(m):
    count = [0, 0, 0]
    a, b = map(int, input().split())

    for j in range(3):
        count[j] = str(prefix[b][j] - prefix[a - 1][j])

    print(" ".join(count))
