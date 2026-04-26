n = int(input())
a = []
t = 0

for i in range(n):
    a.append(list(map(int, input().split())))

a.sort()

for i in range(n):
    t = max(t, a[i][0]) + a[i][1]

print(t)
