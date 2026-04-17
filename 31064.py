import math

n = int(input())
cows = input()
groups = list(cows.split("0"))
original = 0
edgeCount = 0

while "" in groups:
    groups.remove("")

if groups == []:
    print(0)
else:
    maxDays = min(len(groups[0]), len(groups[-1])) - 1
    
    for i in range(0, -2, -1):
        if cows[i] == "0":
            maxDays = min(maxDays, (len(groups[i]) - 1) // 2)

    for i in range(1, len(groups) - 1):
        maxDays = min(maxDays, (len(groups[i]) - 1) // 2)

    for i in range(len(groups)):
        original += math.ceil(len(groups[i]) / (maxDays * 2 + 1))

    print(original)
