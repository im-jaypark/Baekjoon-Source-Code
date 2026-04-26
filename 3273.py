n = int(input())
nums = list(map(int, input().split()))
x = int(input())
numCounts = {}
count = 0

for i in nums:
    try:
        count += numCounts[x - i]
    except:
        pass
    
    try:
        numCounts[i] += 1
    except:
        numCounts[i] = 1

print(count)
