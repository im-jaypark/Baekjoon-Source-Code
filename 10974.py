def dfs(num):
    if len(num) == n:
        print(*num)
    else:
        for i in range(1, n + 1):
            if i not in num:
                dfs(num + [i])

n = int(input())
dfs([])
