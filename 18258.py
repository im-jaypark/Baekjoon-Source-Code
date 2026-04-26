from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    com = sys.stdin.readline().split()
    act = com[0]

    if act == "push":
        queue.append(int(com[1]))
    elif act == "pop":
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif act == "size":
        print(len(queue))
    elif act == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif act == "front":
        try:
            print(queue[0])
        except:
            print(-1)
    else:
        try:
            print(queue[-1])
        except:
            print(-1)
