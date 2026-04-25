n = int(input())
dp = [1, 3]

for i in range(n - 2):
    dp.append(dp[-2] * 2 + dp[-1])

print(dp[n - 1] % 10007)
