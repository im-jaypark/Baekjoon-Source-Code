n = int(input())
nums = []
maxWeights = []

for i in range(n):
    nums.append(int(input()))

nums.sort()

for i in range(n):
    maxWeights.append(nums[i] * (n - i))

print(max(maxWeights))
