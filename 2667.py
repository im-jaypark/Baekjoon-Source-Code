def search(row, column):
    stuck = True
    houseMap[row][column] = 0
    danjis[-1] += 1
    
    if row != 0 and houseMap[row - 1][column] == "1":
        search(row - 1, column)
    if row != n - 1 and houseMap[row + 1][column] == "1":
        search(row + 1, column)

    if column != 0 and houseMap[row][column - 1] == "1":
        search(row, column - 1)
    if column != n - 1 and houseMap[row][column + 1] == "1":
        search(row, column + 1)
    
    
n = int(input())
houseMap = [list(input()) for i in range(n)]
danjis = []

for i in range(n):
    for j in range(n):
        if houseMap[i][j] == "1":
            danjis.append(0)
            search(i, j)

print(len(danjis))
print("\n".join(str(i) for i in sorted(danjis)))
