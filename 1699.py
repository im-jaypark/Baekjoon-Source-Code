n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if int(i ** 0.5) == i ** 0.5:
        dp[i] = 1
    else:
        count = 1
        dp[i] = dp[i - 1] + 1

        while count ** 2 < i:
            dp[i] = min(dp[i], dp[i - count ** 2] + 1)
            count += 1

print(dp[n])
