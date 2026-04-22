t = int(input())

for i in range(t):
    n = int(input())
    counted = 0
    b = len(str(n))
    if n > 9:
        for i in range(2, b):
            counted += int((i - 1) * "5")
        if int(b * "4") < n < int("4" + (b - 1) * "9"):
            counted += n - int(b * "4")
        elif n >= int("4" + (b - 1) * "9"):
            counted += int((b - 1) * "5")
    print(counted)
