nums = []

for i in range(int(input())):
    n = int(input())

    if n == 0:
        nums.pop()
    else:
        nums.append(n)

print(sum(nums))
