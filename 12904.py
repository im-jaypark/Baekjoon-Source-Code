from collections import deque

S = input()
T = deque(input())
direction = -1 #-1: not reversed, 0: reversed

for i in range(len(T) - len(S)):
    if T[direction] == "A":
        if direction == -1:
            T.pop()
        else:
            T.popleft()
    else:
        if direction == -1:
            T.pop()
        else:
            T.popleft()

        direction = -direction - 1

if direction == 0:
    T.reverse()

if "".join(T) == S:
    print(1)
else:
    print(0)
