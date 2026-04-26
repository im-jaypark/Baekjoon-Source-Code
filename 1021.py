from collections import deque

n, m = map(int, input().split())
nums = list(map(int, input().split()))
deq = deque(range(1, n + 1))
count = 0

for i in nums:
    if i == deq[0]:
        deq.popleft()
    else:
        k = deq.index(i)
        count += min(k, n - k)
        deq.rotate(-k)
        deq.popleft()

    n -= 1

print(count)
