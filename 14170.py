def binSearch(start, end, target, direction):
    #print(start, end)
    mid = (start + end) // 2

    if start <= end:
        if haybales[mid] > target:
            if haybales[mid - 1] > target:
                return binSearch(start, mid - 1, target, direction)
            elif haybales[mid - 1] == target:
                return mid - 1
            else:
                if direction == 1:
                    return mid
                else:
                    return mid - 1
        elif haybales[mid] == target:
            return mid
        else:
            return binSearch(mid + 1, end, target, direction)
    else:
        if direction == -1:
            return end
        else:
            return start

N, Q = map(int, input().split())
haybales = sorted(list(map(int, input().split())))

for i in range(Q):
    a, b = map(int, input().split())
    print(binSearch(0, N - 1, b, -1) - binSearch(0, N - 1, a, 1) + 1)
