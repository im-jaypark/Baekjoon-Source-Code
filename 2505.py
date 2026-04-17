def check(start, end, step):
    success = True
    testNums = nums.copy()
    flips = []
    
    for i in range(start, end, step):
        if testNums[i] != i + 1:
            if len(flips) < 2:
                swap = testNums.index(i + 1)

                if swap >= i:
                    testNums[i:swap + 1] = testNums[i:swap + 1][::-1]
                else:
                    testNums[swap:i + 1] = testNums[swap:i + 1][::-1]
                
                flips.append(sorted([i + 1, swap + 1]))
            else:
                success = False
                break

    if success:
        for i in flips:
            print(*i)
        for i in range(2 - len(flips)):
            print(1, 1)
    elif [start, end, step] == [0, n, 1]:
        check(n - 1, -1, -1)

n = int(input())
nums = list(map(int, input().split()))
check(0, n, 1)
