n = int(input())
cards = list(map(int, input().split()))
m = int(input())
toFind = list(map(int, input().split()))
nums = [0] * 20000001
amount = []

for i in cards:
    nums[i + 10 ** 7] += 1

for i in toFind:
    amount.append(str(nums[i + 10 ** 7]))

print(" ".join(amount))
