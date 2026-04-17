import heapq

n = int(input())
nums = []
comps = 0

if n == 1:
    print(0)
else:
    for i in range(n):
        heapq.heappush(nums, int(input()))

    for i in range(n - 2):
        temp = heapq.heappop(nums) + heapq.heappop(nums)
        comps += temp
        heapq.heappush(nums, temp)

    print(comps + sum(nums))
