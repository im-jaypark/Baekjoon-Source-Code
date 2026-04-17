T = int(input())

for i in range(T):
    N = int(input())
    cakes = list(map(int, input().split()))
    totalCakes = sum(cakes)
    left, right = N // 2 - 1, 0
    B, E = 0, sum(cakes[:N // 2 - 1])
    tempE = E

    for j in range(N // 2 - 1):
        left, right = left - 1, right - 1
        tempE = tempE - cakes[left] + cakes[right]
        E = max(E, tempE)

    B = totalCakes - E
    print(B, E)
