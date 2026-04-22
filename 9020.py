for i in range(int(input())):
    n = int(input())
    table = [1] * (n + 1)
    mid = n // 2

    for j in range(2, n + 1):
        if table[j] == 1:
            for k in range(2 * j, n + 1, j):
                table[k] = 0

    for j in range(mid):
        if table[mid + j] == 1 and table[mid - j] == 1:
            print(mid - j, mid + j)
            break
