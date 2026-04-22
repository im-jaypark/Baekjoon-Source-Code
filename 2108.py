n = int(input())
nums = [int(input()) for i in range(n)]
modes = []
nums.sort()
current = ""

for i in nums:
    if i != current:
        modes.append([0, i])
        current = i

    modes[-1][0] += 1

modes.sort(reverse=True)
current = modes[0][0]

for i in range(len(modes)):
    if modes[i][0] != current:
        mode = max(i - 2, 0)
        break
    elif i == len(modes) - 1:
        mode = max(i - 1, 0)

print(round(sum(nums) / n))
print(nums[n // 2])
print(modes[mode][1])
print(nums[-1] - nums[0])
