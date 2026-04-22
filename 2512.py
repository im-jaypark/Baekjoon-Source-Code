import math

def price(budget):
    total = 0

    for i in requests:
        total += min(i, budget)

    return total

def binSearch(low, high):
    mid = math.ceil((low + high) / 2)
    
    if low == high:
        print(low)
    else:
        if price(mid) > M:
            binSearch(low, mid - 1)
        else:
            binSearch(mid, high)
            

N = int(input())
requests = list(map(int, input().split()))
M = int(input()) # actual budget
binSearch(M // N, max(requests))
