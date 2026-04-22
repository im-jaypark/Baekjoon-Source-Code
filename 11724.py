def dfs(x):
    checked[x] = True
    
    for i in nums[x]:
        if not checked[i]:
            dfs(i)

n, m = map(int, input().split())
nums = [[] for i in range(n + 1)]
checked = [False] * (n + 1)
count = 0


for i in range(m):
    u, v = map(int, input().split())
    nums[u].append(v)
    nums[v].append(u)

for i in range(1, n + 1):
    if not checked[i]:
        count += 1
        dfs(i)

print(count)
