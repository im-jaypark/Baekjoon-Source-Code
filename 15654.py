def dfs(num):
    if len(set(num)) == len(num):
        if len(num) == m:
            print(" ".join(num))
        else:
            for i in nums:
                dfs(num + [str(i)])

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
dfs([])
