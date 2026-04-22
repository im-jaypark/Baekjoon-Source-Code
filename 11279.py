import heapq
import sys

input = sys.stdin.readline

nums = []

for i in range(int(input())):
    n = int(input())

    if n == 0:
        try:
            print(-heapq.heappop(nums))
        except:
            print(0)
    else:
        heapq.heappush(nums, -n)
