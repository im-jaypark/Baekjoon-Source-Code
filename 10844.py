n = int(input())
dp = [[0] * 10 for i in range(n)]
dp[0] = [0] + [1] * 9

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][1] += dp[i - 1][0]
        elif j == 9:
            dp[i][8] += dp[i - 1][9]
        else:
            dp[i][j - 1] += dp[i - 1][j]
            dp[i][j + 1] += dp[i - 1][j]

print(sum(dp[-1]) % 10 ** 9)
