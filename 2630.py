def search(size, x, y):
    global zeros
    global ones
    
    section = [table[i][x:x + size] for i in range(y, y + size)]

    if section == [[0] * size] * size:
        zeros += 1
    elif section == [[1] * size] * size:
        ones += 1
    else:
        if size != 1:
            search(size // 2, x, y)
            search(size // 2, x + size // 2, y)
            search(size // 2, x, y + size // 2)
            search(size // 2, x + size // 2, y + size // 2)

n = int(input())
table = [list(map(int, input().split())) for i in range(n)]
zeros = 0
ones = 0

search(n, 0, 0)

print(zeros)
print(ones)
