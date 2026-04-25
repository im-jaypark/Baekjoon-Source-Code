n, m = map(int, input().split())
nums = list(map(int, input().split()))
presum = [0]

for i in nums:
    presum.append(presum[-1] + i)

for i in range(m):
    a, b = map(int, input().split())
    print(presum[b] - presum[a - 1])
