n = int(input())
hansoos = 0

for i in range(1, n + 1):
    if i < 100:
        hansoos += 1
    else:
        difference = int(str(i)[1]) - int(str(i)[0])
        if str(i) == "".join([str(difference * j + int(str(i)[0])) for j in range(len(str(i)))]):
            hansoos += 1

print(hansoos)
