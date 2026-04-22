a, b = map(int, input().split())
count = 1
working = True

while True:
    count += 1

    if a < b:
        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        else:
            working = False
            break
    else:
        working = False
        break

    if a == b:
        break

if working:
    print(count)
else:
    print(-1)
"""
FIRST DRAFT
def dfs(num):
    if len(set(num)) == len(num):
        if len(num) == m:
            print(" ".join(num))
        else:
            for i in range(1, n + 1):
                dfs(num + str(i))

n, m = map(int, input().split())
dfs("")
"""
