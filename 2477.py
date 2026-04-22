n = int(input())
fences = []
counts = [0] * 5
rect = 1
blank = 1

for i in range(6):
    a, b = map(int, input().split())
    counts[a] += 1
    fences.append([a, b])

for i in range(6):
    if counts[fences[i][0]] == 1:
        rect *= fences[i][1]
    else:
        if counts[fences[(i - 1) % 6][0]] == 2:
            if counts[fences[(i + 1) % 6][0]] == 2:
                blank *= fences[i][1]

print(n * (rect - blank))
