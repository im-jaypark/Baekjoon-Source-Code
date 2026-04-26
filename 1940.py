n = int(input())
m = int(input())
materials = list(map(int, input().split()))
locs = {}
count = 0

for i in range(n):
    locs[materials[i]] = 1

for i in range(n):
    if materials[i] != m / 2 and m - materials[i] in locs:
        count += 1

print(count // 2)
