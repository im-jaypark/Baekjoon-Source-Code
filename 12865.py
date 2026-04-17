"""
Solution:
1. Find the max for each value using 1d dp list
2. Using dp, find the best combination for 7
"""
n, k = map(int, input().split())
dp = [0] * (k + 1)
maxCombi = [0] * (k + 1)

for i in range(n):
    w, v = map(int, input().split())

    for j in range(w, k + 1):
        dp[j] = max(dp[j], v)


for i in range(1, k + 1):
    maxi = dp[i]

    for j in range((i + 2) // 2):
        if dp[j] != dp[i - j]:
            maxi = max(maxi, dp[j] + dp[i - j])

    dp[i] = maxi


print(dp[k])
