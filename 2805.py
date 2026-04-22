n, m = map(int, input().split())
trees = list(map(int, input().split()))
lo = 0
hi = max(trees)
mid = (lo + hi) // 2

while lo <= hi:
    lengths = [0, 0]
    
    for i in trees:
        for j in range(2):
            lengths[j] += max(0, i - mid - j)

    if lengths[0] >= m:
        if lengths[1] >= m:
            lo = mid + 1
            mid = (lo + hi) // 2
        else:
            print(mid)
            break
    else:
        hi = mid - 1
        mid = (lo + hi) // 2
