branches = [[int(input())]]
count = 0

while 1 not in branches[0]:
    branches.append([])
    for i in branches[0]:
        if i % 3 == 0:
            branches[1].append(i // 3)
        if i % 2 == 0:
            branches[1].append(i // 2)
        branches[1].append(i - 1)
    del branches[0]
    count += 1

print(count)
