import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    maxStats = [0, 0, 0]
    possible = True

    for j in range(N):
        dayStats = list(map(int, input().split()))

        for k in range(3):
            if dayStats[k] > maxStats[k]:
                maxStats[k] = dayStats[k]
            else:
                dayStats[k] = maxStats[k]
        
        if sum(dayStats[:3]) + j + 1 > dayStats[3]:
            possible = False

    if possible:
        print("YES")
    else:
        print("NO")
