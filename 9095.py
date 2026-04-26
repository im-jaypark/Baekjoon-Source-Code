t = int(input())
possibilities = [1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504]

for i in range(t):
    n = int(input())
    print(possibilities[n - 1])
