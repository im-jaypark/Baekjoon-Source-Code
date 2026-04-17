def checkQuadrant(x, y, side):
    global count
    nextQuadrant = 0
    nextX, nextY = x, y

    if r >= x + 2 ** (side - 1):
        nextQuadrant += 2
        nextX = x + 2 ** (side - 1)
    if c >= y + 2 ** (side - 1):
        nextQuadrant += 1
        nextY = y + 2 ** (side - 1)

    count += nextQuadrant * (4 ** (side - 1))

    if side > 1:
        checkQuadrant(nextX, nextY, side - 1)


n, r, c = map(int, input().split())
count = 0
checkQuadrant(0, 0, n)
print(count)
