for i in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0

    for j in range(n):
        cx, cy, r = map(int, input().split())
        temp = 0

        if ((cx - x1) ** 2 + (cy - y1) ** 2) ** 0.5 <= r:
            temp += 1
        if ((cx - x2) ** 2 + (cy - y2) ** 2) ** 0.5 <= r:
            temp += 1

        count += temp % 2

    print(count)
