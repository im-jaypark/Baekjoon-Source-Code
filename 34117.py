import heapq

n, p = map(int, input().split())
crows = list(map(int, input().split()))
inputs = []
outputs = []
total = 0

for i in range(n):
    total += crows[i]
    heapq.heappush(inputs, crows[i])

    if total >= p:
        while total - inputs[0] >= p:
            total -= heapq.heappop(inputs)

        outputs.append(len(inputs))
    else:
        outputs.append(-1)

print(*outputs)
