N, L = map(int, input().split())
ants = []
lefts = []
rights = []

for i in range(N):
    ant = int(input())
    ants.append([abs(ant), i + 1])

    if ant < 0:
        lefts.append(-ant)
    else:
        rights.append(L - ant)

ants.sort()
lefts.sort()
rights.sort()
leftIndex, rightIndex = 0, 0
antsIndexes = [0, N - 1]

for i in range(N):
    if leftIndex >= len(lefts):
        fallAnt = ants[antsIndexes[1]]
        antsIndexes[1] -= 1
        fallTime = rights[rightIndex]
        rightIndex += 1
    elif rightIndex >= len(rights):
        fallAnt = ants[antsIndexes[0]]
        antsIndexes[0] += 1
        fallTime = lefts[leftIndex]
        leftIndex += 1
    elif lefts[leftIndex] < rights[rightIndex]:
        fallAnt = ants[antsIndexes[0]]
        antsIndexes[0] += 1
        fallTime = lefts[leftIndex]
        leftIndex += 1
    else:
        fallAnt = ants[antsIndexes[1]]
        antsIndexes[1] -= 1
        fallTime = rights[rightIndex]
        rightIndex += 1

print(fallAnt[1], fallTime)

# Left facing falls: leftmost one
# Right facing falls: rightmost one
# Ants fall at different tiems
# No ants share housing

# First draft error: assumed that for each ant, they will last
# the amount of time from the start to their designated edge (so no collision)
