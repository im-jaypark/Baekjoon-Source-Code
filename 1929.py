n, m = map(int, input().split())
nums = [False for i in range(2)] + [True for i in range(m - 1)]

for i in range(2, m // 2 + 1):
    if nums[i] == True:
        for j in range(i * 2, m + 1, i):
            nums[j] = False

for i in range(n, m + 1):
    if nums[i]:
        print(i)
