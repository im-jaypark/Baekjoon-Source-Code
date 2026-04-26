def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True

n = int(input())
nums = list(map(int, input().split()))

if n == 2:
    nums.sort()
    
    if nums[0] == 1 and prime(nums[1]):
        print("NO")
    else:
        print("YES")
        print(2)
        print(*nums)
else:
    nonOne = []

    for i in nums:
        if i != 1:
            nonOne.append(i)

        if len(nonOne) == 2:
            break

    print("YES")
    print(2)
    print(*nonOne)
