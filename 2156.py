n = int(input())
wines = [0] + [int(input()) for i in range(n)]
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i <= 2:
        dp[i] = sum(wines[i - 1:i + 1])
    else:
        onePre = max(dp[max(i - 4, 0):i - 1])
        twoPre = max(dp[max(i - 5, 0):i - 2])
        dp[i] = max(onePre + wines[i], twoPre + sum(wines[i - 1:i + 1]))

print(max(dp[-3:]))
