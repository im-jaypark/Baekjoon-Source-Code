T = int(input())

for i in range(T):
    N = int(input())
    ranks = sorted([tuple(map(int, input().split())) for j in range(N)])
    minRound2 = ranks[0][1]
    employees = 1

    for j in range(1, N):
        if ranks[j][1] < minRound2:
            minRound2 = ranks[j][1]
            employees += 1

    print(employees)
