N = int(input())
nums = []

for i in range(1, N + 1, 2):
    nums.append(i)

for i in range(N // 2 * 2, 1, -2):
    nums.append(i)

print(*nums)
