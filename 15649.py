def dfs(num):
    if len(set(num)) == len(num):
        if len(num) == m:
            print(" ".join(num))
        else:
            for i in range(1, n + 1):
                dfs(num + str(i))

n, m = map(int, input().split())
dfs("")
