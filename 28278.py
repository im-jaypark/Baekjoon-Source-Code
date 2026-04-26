from collections import deque
import sys

input = sys.stdin.readline
stack = deque()

for i in range(int(input())):
    n = list(map(int, input().split()))

    if n[0] == 1:
        stack.append(n[1])
    elif n[0] == 2:
        try:
            print(stack.pop())
        except:
            print(-1)
    elif n[0] == 3:
        print(len(stack))
    elif n[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        try:
            print(stack[-1])
        except:
            print(-1)
