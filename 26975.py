n = int(input())
tuis = sorted(list(map(int, input().split())))
t = []

for i in range(n):
    t.append(tuis[i] * (n - i))

print(max(t), tuis[t.index(max(t))])
