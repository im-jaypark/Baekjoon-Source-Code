cows = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cowsIndex = [[] for i in range(26)]
crossings = 0

for i in range(52):
    cowsIndex[alphabet.index(cows[i])].append(i)

for i in range(26):
    for j in range(i + 1, 26):
        cowsBetween = 0

        for k in range(2):
            if cowsIndex[i][0] < cowsIndex[j][k] < cowsIndex[i][1]:
                cowsBetween += 1

        if cowsBetween == 1:
            crossings += 1

print(crossings)
