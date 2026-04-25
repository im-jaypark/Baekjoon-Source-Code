def dfs(num):
    if len(num) == m + 1:
        print(" ".join(num[1:]))
    else:
        for i in range(int(num[-1]), n + 1):
            dfs(num + str(i))

n, m = map(int, input().split())
dfs("1")
