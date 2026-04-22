n = int(input())
houses = [0] * n
comp = [[1, 2], [0, 2], [0, 1]]
dp = [[0, 0, 0]]

for i in range(n):
    houses[i] = list(map(int, input().split()))
    dp.append([0, 0, 0])

    for j in range(3):
        dp[i + 1][j] = houses[i][j] + min(dp[i][comp[j][0]], dp[i][comp[j][1]])

print(min(dp[n]))
