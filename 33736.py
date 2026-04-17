n = int(input())
a = list(map(int, input().split()))
types = set(a)
count = [0] * (n + 1)
missing = [0] * (n + 1)

for i in a:
    count[i] += 1

for i in range(n):
    missing[i + 1] = missing[i]

    if count[i] == 0:
        missing[i + 1] += 1

for i in range(n + 1):
    print(max(count[i], missing[i]))
