import heapq
import sys
input = sys.stdin.readline

n = int(input())
posheap = []
negheap = []

for i in range(n):
    k = int(input())

    if k == 0:
        if [] in (posheap, negheap):
            if (posheap, negheap) == ([], []):
                print(0)
            else:
                try:
                    print(heapq.heappop(posheap))
                except:
                    print(-heapq.heappop(negheap))
        else:
            if posheap[0] < negheap[0]:
                print(heapq.heappop(posheap))
            else:
                print(-heapq.heappop(negheap))
    elif k > 0:
        heapq.heappush(posheap, k)
    else:
        heapq.heappush(negheap, -k)
