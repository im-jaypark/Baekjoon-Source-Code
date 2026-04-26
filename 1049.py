n, m = map(int, input().split())
mins = []

for i in range(m):
    six, one = map(int, input().split())

    if i == 0:
        mins = [six, one]
    else:
        mins[0] = min(mins[0], six)
        mins[1] = min(mins[1], one)

sixes = n // 6 * (min(mins[0], 6 * mins[1]))
ones = min(mins[0], n % 6 * mins[1])

print(sixes + ones)
