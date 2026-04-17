n = int(input())
coords = [list(map(int, input().split())) for i in range(n)]
minY = min([i[1] for i in coords])
maxY = max([i[1] for i in coords])
loHypCoords = []
hiHypCoords = []

#Lowest is hypotenuse

for i in coords:
    loHypCoords.append(i[0] + i[1] - minY)
    loHypCoords.append(i[0] - i[1] + minY)

xLen = max(loHypCoords) - min(loHypCoords)

#Highest is hypotenuse

for i in coords:
    hiHypCoords.append(i[0] + maxY - i[1])
    hiHypCoords.append(i[0] - maxY + i[1])

xLen = min(xLen, max(hiHypCoords) - min(hiHypCoords))

print(max(xLen, 2 * (maxY - minY)))
