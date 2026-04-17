n = int(input())
cows = [0] * (n + 1)
locations = [[-1, -1] for i in range(7)]
checks = [False] * 7
count = 0

for i in range(1, n + 1):
    cows[i] = cows[i - 1]
    cows[i] += int(input())
    cows[i] %= 7

for i in range(n + 1):
    if locations[cows[i]][0] == -1:
        locations[cows[i]][0] = i
        checks[cows[i]] = True
        count += 1

    if count == 7:
        break

count = 0

for i in range(n, -1, -1):
    if locations[cows[i]][1] == -1:
        locations[cows[i]][1] = i
        count += 1

    if count == 7:
        break

for i in range(7):
    if checks[i]:
        locations[i] = locations[i][1] - locations[i][0]
    else:
        locations[i] = 0

print(max(locations))
