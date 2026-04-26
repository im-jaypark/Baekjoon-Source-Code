for i in range(int(input())):
    clothes = {}
    total = 1

    for j in range(int(input())):
        clothing = input().split()[1]

        try:
            clothes[clothing] += 1
        except:
            clothes[clothing] = 2

    for j in clothes.values():
        total *= j

    print(total - 1)
