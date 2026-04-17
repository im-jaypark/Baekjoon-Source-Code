import math

def possible(dist):
    routers = 1
    closest = houses[0]

    for i in range(1, n):
        if houses[i] - closest >= dist:
            routers += 1
            closest = houses[i]

    if routers >= c:
        return True
    else:
        return False

def binSearch(start, end):
    mid = math.ceil((start + end) / 2)
    if start == end:
        print(start)
    elif possible(mid):
        binSearch(mid, end)
    else:
        binSearch(start, mid - 1)

n, c = map(int, input().split())
houses = sorted([int(input()) for i in range(n)])
houseRange = houses[-1] - houses[0]

binSearch(1, houseRange)
