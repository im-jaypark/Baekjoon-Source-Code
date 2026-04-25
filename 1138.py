N = int(input())
tallers = list(map(int, input().split()))
line = [0] * N

for i in range(N):
    blanks = 0

    for j in range(N):
        if line[j] == 0:
            if blanks == tallers[i]:
                line[j] = i + 1
                break
            blanks += 1

print(*line)
