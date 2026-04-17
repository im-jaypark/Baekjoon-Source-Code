import heapq, sys
input = sys.stdin.readline

N, k = map(int, input().split())
total = 0
counters = [[0, i, 0] for i in range(k)]
exits = []
sameExit = []

for i in range(N + k):
    if i < N:
        ID, items = map(int, input().split())
    
    counter = heapq.heappop(counters)
    
    if sameExit and counter[0] != sameExit[-1][0]:
        for j in range(len(sameExit)):
            exits.append(sameExit.pop()[2])
    
    sameExit.append(counter.copy())
    
    if i < N:
        counter[0] += items
        counter[2] = ID
    else:
        counter[0] = float("inf")

    heapq.heappush(counters, counter)

for i in range(len(sameExit)):
    exits.append(sameExit.pop()[2])

for i in range(1, N + 1):
    total += i * exits[i + k - 1]

print(total)
