def dfs(current, remaining):
    if sum(remaining) == 0:
        result = calc(current)
        minMax[0] = min(minMax[0], result)
        minMax[1] = max(minMax[1], result)
    else:
        for i in range(4):
            if remaining[i]:
                remaining[i] -= 1
                dfs(current + [i], remaining)
                remaining[i] += 1
                
def calc(opers):
    outcome = nums[0]
    
    for i in range(N - 1):
        if opers[i] == 0:
            outcome += nums[i + 1]
        elif opers[i] == 1:
            outcome -= nums[i + 1]
        elif opers[i] == 2:
            outcome *= nums[i + 1]
        elif outcome >= 0:
            outcome //= nums[i + 1]
        else:
            outcome = -(-outcome // nums[i + 1])
    
    return outcome

N = int(input())
nums = list(map(int, input().split()))
operCount = list(map(int, input().split()))
minMax = [float("inf"), -float("inf")]
dfs([], operCount)

print(minMax[1])
print(minMax[0])
