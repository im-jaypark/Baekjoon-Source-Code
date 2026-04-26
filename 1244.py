import math

n = int(input())
switches = list(map(int, input().split()))
students = int(input())

for i in range(students):
    gender, switchNum = list(map(int, input().split()))

    if gender == 1:
        for j in range(switchNum - 1, n, switchNum):
            switches[j] = -switches[j] + 1
    else:
        switches[switchNum - 1] = -switches[switchNum - 1] + 1
        for j in range(1, min(switchNum - 1, n - switchNum) + 1):
            if switches[switchNum - 1 + j] == switches[switchNum - 1 - j]:
                switches[switchNum - 1 + j] = -switches[switchNum - 1 + j] + 1
                switches[switchNum - 1 - j] = -switches[switchNum - 1 - j] + 1
            else:
                break

for i in range(math.ceil(n / 20)):
    print(*switches[i * 20: min((i + 1) * 20, n)])
