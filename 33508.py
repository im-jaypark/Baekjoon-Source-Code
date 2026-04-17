n = int(input())
text = list(map(int, input().split()))
nums = set()
count = {}
moos = 0

for i in set(text):
    count[str(i)] = 0

for i in text:
    count[str(i)] += 1

for i in text:
    nums.add(i)

    if count[str(i)] == 2:
        moos += len(nums) - int(i in nums)

    count[str(i)] -= 1

print(moos)
