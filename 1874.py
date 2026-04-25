from collections import deque

n = int(input())
goal = deque([int(input()) for i in range(n)])
s = deque()
q = deque(list(range(1, n + 1)))
steps = deque()
possible = True

for i in goal:
    if i >= q[0] and (len(s) == 0 or s[-1] != i):
        for j in range(i - q[0] + 1):
            deque.append(s, deque.popleft(q))
            deque.append(steps, "+")

        deque.append(q, deque.pop(s))
        deque.append(steps, "-")
    else:
        if s[-1] == i:
            deque.append(q, deque.pop(s))
            deque.append(steps, "-")
        else:
            possible = False
            break

if possible:
    for i in steps:
        print(i)
else:
    print("NO")
