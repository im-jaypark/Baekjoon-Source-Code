Q = int(input())

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        c, t = query[1:]

        if t <= 3 * c - 1:
            print(min(c, 3 * c - 1 - t))
        else:
            zeros = [3 * c - 1]

            while t > zeros[-1]:
                zeros.append(zeros[-1] + 1 + (zeros[-1] + 1) // 2)

            print(zeros[-1] - t)
    else:
        x, t = query[1:]

        if t <= 2 * x - 1:
            print(x)
        else:
            x, t = 0, x + t

            while True:
                if t % 3 == 2:
                    print((t + 1) // 3)
                    break
                else:
                    t -= t // 3 + 1
