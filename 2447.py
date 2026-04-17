def pattern(size):
    if size == 1:
        return ["*"]
    
    smaller = pattern(size // 3)
    bigger = [[" "] * size for i in range(size)]
    
    for i in range(3):
        for row in range(size // 3):
            addRow = size * i // 3 + row
            for j in range(3):
                start = size * j // 3
                end = size * (j + 1) // 3
                if (i, j) != (1, 1):
                    bigger[addRow][start:end] = smaller[row]
    
    return bigger

N = int(input())

for row in pattern(N):
    print("".join(row))
