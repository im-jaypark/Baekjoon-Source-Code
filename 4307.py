T = int(input())

for i in range(T):
    l, n = map(int, input().split())
    ants = [min(i, l - i) for i in [int(input()) for j in range(n)]]
    print(max(ants), l - min(ants))
