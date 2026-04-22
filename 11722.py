n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    maxLen = 0
    
    for j in range(i):
        if nums[j] > nums[i]:
            maxLen = max(maxLen, dp[j])
    
    dp[i] = maxLen + 1

print(max(dp))
