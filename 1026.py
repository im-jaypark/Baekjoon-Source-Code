n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
nums = [0] * n

for i in range(n):
    nums[i] = a[i] * b[i]

print(sum(nums))
