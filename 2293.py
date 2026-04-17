n, k = map(int, input().split())
coins = sorted([int(input()) for i in range(n)])
dp = [0] * (k + 1)

for coinValue in coins:
    if coinValue <= k:
        dp[coinValue] += 1

        for j in range(coinValue + 1, k + 1):
            dp[j] += dp[j - coinValue]

print(dp[k])
