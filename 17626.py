"""
# First Draft

n = int(input())
dp = [0] + [5] * n

for i in range(1, n + 1):
    if int(i ** 0.5) == i ** 0.5:
        dp[i] = 1
    else:
        for j in range(1, i // 2 + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])

            if dp[i] == 2:
                break

print(dp[n])
"""
n = int(input())
dp = [0] + [5] * n

for i in range(4):
    for j in range(n + 1):
        if dp[j] == i:
            for k in range(1, int((n - j) ** 0.5) + 1):
                dp[j + k ** 2] = min(i + 1, dp[j + k ** 2])

print(dp[n])
