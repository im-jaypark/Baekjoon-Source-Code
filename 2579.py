n = int(input())
stairs = [int(input()) for i in range(n)]
maxScores = []

for i in range(n):
    if i < 2:
        maxScores.append(sum(stairs[0:i + 1]))
    elif i == 2:
        maxScores.append(max(stairs[i] + maxScores[i - 2], sum(stairs[i - 1:i + 1])))
    else:
        maxScores.append(max(stairs[i] + maxScores[i - 2], sum(stairs[i - 1:i + 1]) + maxScores[i - 3]))

print(maxScores[n - 1])
