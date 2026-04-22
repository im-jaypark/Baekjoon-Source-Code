while True:
    n = int(input())

    if n == 0:
        break
    
    nums = [0] * 2 + [1] * (2 * n - 1)

    for i in range(2, 2 * n + 1):
        for j in range(2 * i, 2 * n + 1, i):
            nums[j] = 0

    print(sum(nums[n + 1:]))
