n = int(input())
coords = list(map(int, input().split()))
distinct = sorted(set(coords))
d = {}

for i in range(len(distinct)):
    d[distinct[i]] = i

for i in range(n):
    coords[i] = d[coords[i]]

print(*coords)
