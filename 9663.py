def dfs(queens):
    global ways

    if len(queens) != n:
        for i in range(n):
            if i not in queens:
                possible = True
                
                for j in range(len(queens)):
                    if abs(queens[j] - i) == abs(j - len(queens)):
                        possible = False
                        break

                if possible:
                    dfs(queens + [i])
    else:
        ways += 1

n = int(input())
ways = 0

dfs([])
print(ways)
