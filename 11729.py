n = int(input())
forwards = [[1, 2], [2, 3], [3, 1]]
backwards = [[1, 3], [2, 1], [3, 2]]
counts = [0] * (n + 1)

print(2 ** n - 1)

for i in range(1, 2 ** n):
    for j in range(n - 1, -1, -1):
        if i % (2 ** j) == 0:
            if (n - j) % 2 == 0:
                print(*forwards[counts[j]])
                counts[j] = (counts[j] + 1) % 3
            else:
                print(*backwards[counts[j]])
                counts[j] = (counts[j] - 1) % 3

            break
