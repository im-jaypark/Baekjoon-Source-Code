T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    r = input()
    varCounts = [[1, 0] for i in range(K)]
    lastChanged = [0] * K

    for j in range(N - K):
        if r[j] == r[j + 1]:
            varCounts[j % K][lastChanged[j % K]] += 1
        else:
            varCounts[j % K][-lastChanged[j % K] + 1] += 1
            lastChanged[j % K] = -lastChanged[j % K] + 1

    maxDp = [varCounts[0][::-1]] + [[0, 0] for i in range(K - 1)]
    minDp = [varCounts[0][::-1]] + [[0, 0] for i in range(K - 1)]

    for j in range(1, K):
        maxDp[j][0] = max(varCounts[j][0] + maxDp[j - 1][1],
                          varCounts[j][1] + maxDp[j - 1][0])
        maxDp[j][1] = max(varCounts[j][0] + maxDp[j - 1][0],
                          varCounts[j][1] + maxDp[j - 1][1])
        minDp[j][0] = min(varCounts[j][0] + minDp[j - 1][1],
                          varCounts[j][1] + minDp[j - 1][0])
        minDp[j][1] = min(varCounts[j][0] + minDp[j - 1][0],
                          varCounts[j][1] + minDp[j - 1][1])

    print(minDp[-1][int(r[0])], maxDp[-1][int(r[0])])
