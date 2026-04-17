n, u = map(int, input().split())
endP = n - 1
half = n // 2
canvas = [" ".join(input()).split() for i in range(n)]
toChange = [[0 for j in range(half)] for i in range(half)]
score = {"0": 0, "1": 1, "2": 2, "3": 1, "4": 0}
total = 0

for i in range(half):
    for j in range(half):
        temp = 0
        
        if canvas[i][j] == "#":
            temp += 1
        if canvas[endP - i][j] == "#":
            temp += 1
        if canvas[i][endP - j] == "#":
            temp += 1
        if canvas[endP - i][endP - j] == "#":
            temp += 1

        toChange[i][j] = temp
        total += score[str(temp)]

print(total)

for i in range(u):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    row = r
    column = c

    if row >= half:
        row = endP - row
    if column >= half:
        column = endP - column

    temp = toChange[row][column]
    
    if canvas[r][c] == "#":
        canvas[r][c] = "."
        toChange[row][column] -= 1
    else:
        canvas[r][c] = "#"
        toChange[row][column] += 1

    total += score[str(toChange[row][column])] - score[str(temp)]
    print(total)
