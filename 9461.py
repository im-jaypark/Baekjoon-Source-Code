t = int(input())
dp = [0, 1, 1, 1, 2]

for i in range(t):
    n = int(input())

    for i in range(n - len(dp) + 1):
        dp.append(dp[-1] + dp[-5])

    print(dp[n])
