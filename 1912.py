n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]] + [0] * (n - 1)
hi = nums[0]

for i in range(1, n):
    if dp[i - 1] > 0:
        dp[i] = dp[i - 1] + nums[i]
    else:
        dp[i] = nums[i]

    hi = max(hi, dp[i])

print(hi)
