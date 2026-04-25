t = int(input())

for i in range(t):
    n = int(input())
    cows = list(map(int, input().split()))
    count = {}
    hi = max(cows)
    pairs = 0

    for j in cows:
        if j != hi:
            try:
                count[j] += 1
            except:
                count[j] = 1

    for i in list(count.values()):
        if i >= 2:
            pairs += 2

    print(pairs + 1)
