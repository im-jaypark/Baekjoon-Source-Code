n = int(input())
dp = [0] * (n + 1)

for i in range(n):
    t, p = map(int, input().split())

    try:
        for j in range(i + t, n + 1):
            dp[j] = max(dp[i] + p, dp[j])
    except:
        pass

print(dp[n])
