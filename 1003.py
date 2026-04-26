t = int(input())
zeros = [1, 0]
ones = [0, 1]
nums = []

for i in range(t):
    nums.append(int(input()))

    if nums[-1] > len(zeros) - 1:
        for i in range(nums[-1] - len(zeros) + 1):
            zeros.append(zeros[-1] + zeros[-2])
            ones.append(ones[-1] + ones[-2])
    
    print(zeros[nums[-1]], ones[nums[-1]])
