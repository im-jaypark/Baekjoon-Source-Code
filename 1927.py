import heapq
import sys

input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    x = int(input())

    if x == 0:
        if nums == []:
            print(0)
        else:
            print(heapq.heappop(nums))
    else:
        heapq.heappush(nums, x)
