import sys
input = sys.stdin.readline

def dimensions(tetromino):
    l1, w1 = 0, 0

    for block in tetromino:
        l1 = max(block[0], l1)
        w1 = max(block[1], w1)

    return (l1, w1)

L = [((0, 0), (0, 1), (0, 2), (1, 2)), ((0, 0), (1, 0), (2, 0), (0, 1)),
     ((0, 0), (1, 0), (1, 1), (1, 2)), ((2, 0), (0, 1), (1, 1), (2, 1)),
     ((1, 0), (1, 1), (0, 2), (1, 2)), ((0, 0), (1, 0), (2, 0), (2, 1)),
     ((0, 0), (1, 0), (0, 1), (0, 2)), ((0, 0), (0, 1), (1, 1), (2, 1))]
S = [((0, 0), (0, 1), (1, 1), (1, 2)), ((1, 0), (2, 0), (0, 1), (1, 1)),
     ((1, 0), (0, 1), (1, 1), (0, 2)), ((0, 0), (1, 0), (1, 1), (2, 1))] 
T = [((0, 0), (0, 1), (1, 1), (0, 2)), ((0, 0), (1, 0), (2, 0), (1, 1)),
     ((1, 0), (0, 1), (1, 1), (1, 2)), ((1, 0), (0, 1), (1, 1), (2, 1))]
I = [((0, 0), (0, 1), (0, 2), (0, 3)), ((0, 0), (1, 0), (2, 0), (3, 0))]
O = [((0, 0), (1, 0), (0, 1), (1, 1))]

tetrominoes = (L, S, T, I, O)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]
high = 0

for tetro in tetrominoes:
    for fixed in tetro:
        l, w = dimensions(fixed)

        for y in range(n - w):
            for x in range(m - l):
                tempTotal = 0
                
                for block in fixed:
                    tempTotal += grid[y + block[1]][x + block[0]]

                high = max(high, tempTotal)

print(high)
