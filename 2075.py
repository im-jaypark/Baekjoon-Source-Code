import heapq

n = int(input())
topFive = []

for i in range(n):
    row = list(map(int, input().split()))
    
    if i == 0:
        topFive = row.copy()
    else:
        for j in range(n):
            heapq.heappush(topFive, row[j])
            heapq.heappop(topFive)

print(heapq.heappop(topFive))
