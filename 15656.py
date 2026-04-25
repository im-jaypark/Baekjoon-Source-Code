def dfs(x):
    if len(x) == m:
        print(*x)
    else:
        for i in nums:
            dfs(x + [i])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
dfs([])
