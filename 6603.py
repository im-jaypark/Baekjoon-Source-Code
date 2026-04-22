def dfs(n, ind):
    if len(n) == 6:
        print(*n)
    else:
        for i in range(len(n) - ind + k - 5):
            dfs(n + [s[ind + i]], ind + i + 1)

first = True
while True:
    k, *s = list(map(int, input().split()))

    if k == 0:
        break
    else:
        if first:
            first = False
        else:
            print()

        dfs([], 0)
