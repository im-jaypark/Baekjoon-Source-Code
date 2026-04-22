n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    add = 0
    
    for j in range(i):

        if nums[j] < nums[i]:
            add = max(add, dp[j])

    dp[i] = add + 1

print(max(dp))
