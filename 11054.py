n = int(input())
nums = [0] + list(map(int, input().split()))
leftDP = [0] * (n + 1)
leftLasts = [[i] for i in nums]
rightDP = [0] * (n + 1)
rightLasts = [[i] for i in [0] + nums[:0:-1]]
lbs = 0

# finding the increasing subsequence from the left
for i in range(1, n + 1):
    maxLen = 0
    
    for j in range(1, i):
        if nums[j] < nums[i]:
            maxLen = max(maxLen, leftDP[j])

    leftDP[i] = maxLen + 1

for i in range(1, n + 1):
    if leftDP[i - 1] > leftDP[i]:
        leftDP[i] = leftDP[i - 1]
        leftLasts[i] = leftLasts[i - 1].copy()
    elif leftDP[i - 1] == leftDP[i]:
        leftLasts[i] = leftLasts[i - 1].copy() + [nums[i]]
    else:
        leftLasts[i] = [nums[i]]

nums = [0] + nums[:0:-1]

# finding the increasing subsequence from the right
for i in range(1, n + 1):
    maxLen = 0
   
    for j in range(1, i):
        if nums[j] < nums[i]:
            maxLen = max(maxLen, rightDP[j])

    rightDP[i] = maxLen + 1

for i in range(1, n + 1):
    if rightDP[i - 1] > rightDP[i]:
        rightDP[i] = rightDP[i - 1]
        rightLasts[i] = rightLasts[i - 1].copy()
    elif rightDP[i - 1] == rightDP[i]:
        rightLasts[i] = rightLasts[i - 1].copy() + [nums[i]]
    else:
        rightLasts[i] = [nums[i]]

for i in range(n + 1):
    # special case: the middle values are the same: nonbitonic
    tempLeftLasts = set(leftLasts[i])
    tempRightLasts = set(rightLasts[n - i])
    oneOption = (len(tempLeftLasts), len(tempRightLasts)) == (1, 1)
    sameOption = tempLeftLasts == tempRightLasts
   
    if oneOption and sameOption:
        # Both have 1 option and their options are the same: remove 1
        lbs = max(lbs, leftDP[i] + rightDP[-i - 1] - 1)
    else:
        lbs = max(lbs, leftDP[i] + rightDP[-i - 1])

print(lbs)
