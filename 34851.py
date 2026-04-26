n = int(input())
nums = list(map(int, input().split()))
answer = nums[0]
mod = 10 ** 9 + 7
reachedMod = False

for i in range(1, n + 1):
    if reachedMod:
        if nums[i] == 1:
            answer = (answer + nums[i]) % mod
        else:
            answer = (answer * nums[i]) % mod
    else:
        if max(answer + nums[i], answer * nums[i]) >= mod:
            reachedMod = True

        answer = max(answer + nums[i], answer * nums[i]) % mod

print(answer)
