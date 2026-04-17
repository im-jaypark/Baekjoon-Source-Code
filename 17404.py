n = int(input())
houses = [0] * n
comp = [[1, 2], [0, 2], [0, 1]]
cans = [0] * 3

for i in range(n):
    houses[i] = list(map(int, input().split()))

for i in range(3):
    dp = [[0] * 3 for j in range(n)]

    for j in range(3):
        if j == i:
            dp[1][j] = 2000
        else:
            dp[1][j] = houses[1][j] + houses[0][i]
    
    for j in range(2, n):
        for k in range(3):
            if not (j == n - 1 and k == i):
                mini = min(dp[j - 1][comp[k][0]], dp[j - 1][comp[k][1]])
                dp[j][k] = houses[j][k] + mini
            else:
                dp[j][k] = 10 ** 6
                

    cans[i] = min(dp[-1])

print(min(cans))
