n = int(input())
nums = [[int(input())]]
best = nums.copy()

for i in range(1, n):
    nums.append(list(map(int, input().split())))
    best.append([0] * (i + 1))

    for j in range(i):
        best[i][j] = max(best[i][j], best[i - 1][j] + nums[i][j])
        best[i][j + 1] = max(best[i][j + 1], best[i - 1][j] + nums[i][j + 1])

print(max(best[-1]))
