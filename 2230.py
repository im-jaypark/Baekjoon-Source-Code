n, m = map(int, input().split())
nums = []
r = n - 1
l = n - 2

for i in range(n):
    nums.append(int(input()))

if n > 1:
    nums.sort()
    ans = nums[-1] - nums[0]

    while l > 0 or nums[r] - nums[l] >= m:
        dif = nums[r] - nums[l]
        if dif == m:
            ans = m
            break
        elif dif > m and r - l >= 1:
            ans = min(ans, dif)
            r -= 1
        elif l > 0:
            l -= 1
        else:
            break

    print(ans)
else:
    print(0)
