n, m = map(int, input().split())
nums = list(map(int, input().split()))
preSum = [0]
count = 0

for i in range(n):
    preSum.append(preSum[-1] + nums[i])

for i in range(1, n + 1):
    count += preSum[:i + 1].count(preSum[i] - m)

print(count)
