N, M = map(int, input().split())
order = list(range(N + 1))

for i in range(M):
    x, y = map(int, input().split())
    order[x] += 1
    order[y] -= 1

if len(set(order[1:])) == N:
    print(*order[1:])
else:
    print(-1)
