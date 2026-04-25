import sys

def count(leng):
    pieces = 0

    for i in lans:
        pieces += i // leng

    return pieces

n, k = map(int, input().split())
lans = [int(input()) for i in range(n)]
lo = 1
hi = sum(lans) // k
mid = (lo + hi) // 2

while lo <= hi:
    for i in [lo, hi]:
        if count(i) >= k and count(i + 1) < k:
            print(i)
            sys.exit()

    if count(mid) >= k:
        if count(mid + 1) < k:
            print(mid)
            sys.exit()
        else:
            lo = mid + 1
            mid = (lo + hi) // 2
    else:
        hi = mid - 1
        mid = (lo + hi) // 2
