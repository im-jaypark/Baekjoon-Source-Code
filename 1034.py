N, M = map(int, input().split())
table = [list(map(int, " ".join(input()).split())) for i in range(N)]
counts = [i.count(0) for i in table]
K = int(input())
maxLamps = 0

for i in range(N):
    if counts[i] % 2 == K % 2 and K >= counts[i]:
        sums = [sum(table[i]) for i in range(N)]
        
        for j in range(M):
            if table[i][j] == 0:
                for k in range(N):
                    if table[k][j] == 1:
                        sums[k] -= 1
                    else:
                        sums[k] += 1

        maxLamps = max(maxLamps, sums.count(M))

print(maxLamps)
