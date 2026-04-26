for i in range(int(input())):
    a, b, c, d, e, f = list(map(int, input().split()))
    dis = ((a - d) ** 2 + (b - e) ** 2) ** 0.5
    sides = sorted([dis, c, f])

    if dis != 0:
        if sides[2] > sides[0] + sides[1]:
            locs = 0
        elif sides[2] == sides[0] + sides[1]:
            locs = 1
        else:
            locs = 2
    else:
        if c == f:
            locs = -1
        else:
            locs = 0

    print(locs)
