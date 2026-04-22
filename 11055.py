N = int(input())
nums = list(map(int, input().split()))
dp = []

for i in range(N):
    maxPrev = 0

    for j in range(i):
        if nums[j] < nums[i]:
            maxPrev = max(maxPrev, dp[j])

    dp.append(maxPrev + nums[i])

print(max(dp))
