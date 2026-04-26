n, k = map(int, input().split())
nums = list(map(int, input().split()))
pfs = [nums[0]]

for i in range(1, n):
    pfs.append(pfs[-1] + nums[i])

hi = pfs[k - 1]

for i in range(k, n):
    hi = max(hi, pfs[i] - pfs[i - k])

print(hi)
