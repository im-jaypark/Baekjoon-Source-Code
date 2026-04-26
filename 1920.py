n = int(input())
nums = sorted(list(map(int, input().split())))
m = int(input())
findThese = list(map(int, input().split()))

for i in findThese:
    found = 0
    start = 0
    end = n
    
    while end - start > 0:
        point = (start + end) // 2
        if nums[point] == i or nums[start] == i or nums[end - 1] == i:
            found = 1
            break
        elif nums[point] < i:
            start = point + 1
        else:
            end = point

    print(found)
