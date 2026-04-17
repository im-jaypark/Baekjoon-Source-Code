from heapq import *
import sys

input = sys.stdin.readline

N = int(input())
half1 = []
half2 = []

for i in range(N):
    num = int(input())

    if i % 2 == 0:
        heappush(half2, num)
        heappush(half1, -heappop(half2))
    else:
        heappush(half1, -num)
        heappush(half2, -heappop(half1))

    print(-half1[0])
