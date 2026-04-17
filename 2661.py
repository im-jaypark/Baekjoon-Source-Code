def dfs(n):
    global printed
    good = True
    count = len(n)

    for i in range(1, count // 2 + 1):
        if n[count - (2 * i):count - i] == n[count - i:count]:
            good = False
            break

    if good and not printed:
        if count == num:
            printed = True
            print(n)
        else:
            for i in range(1, 4):
                dfs(n + str(i))

num = int(input())
printed = False
dfs("1")
