n = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))
total = 0
low = costs[0]

for i in range(n - 1):
    if costs[i] < low:
        low = costs[i]

    total += low * dists[i]

print(total)
