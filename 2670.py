n = int(input())
nums = []
maxProd = 0

for i in range(n):
    nums.append(float(input()))

for i in range(n):
    temp = 1
    for j in range(n - i):
        temp *= nums[i + j]
        maxProd = max(temp, maxProd)
    
maxProd = round(maxProd, 3)

print(maxProd, "0" * (3 - len(str(maxProd).split(".")[1])), sep="")
