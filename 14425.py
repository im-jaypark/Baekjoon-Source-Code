n, m = map(int, input().split())
sites = {}
count = 0

for i in range(n):
    sites[input()] = 1

for i in range(m):
    try:
        count += sites[input()]
    except:
        pass

print(count)
