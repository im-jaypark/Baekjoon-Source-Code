def dfs(num):
    if len(num) == m:
        print(" ".join(num))
    else:
        for i in nums:
            try:
                if i > int(num[-1]):
                    dfs(num + [str(i)])
            except:
                dfs(num + [str(i)])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
dfs([])
