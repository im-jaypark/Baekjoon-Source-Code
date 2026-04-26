from collections import deque

n = int(input())
deq = deque()

for i in range(n):
    com = input().split()
    act = com[0]

    if act == "push_front":
        deq.appendleft(com[1])
    elif act == "push_back":
        deq.append(com[1])
    elif act == "pop_front":
        try:
            print(deq.popleft())
        except:
            print(-1)
    elif act == "pop_back":
        try:
            print(deq.pop())
        except:
            print(-1)
    elif act == "size":
        print(len(deq))
    elif act == "empty":
        print(int(not bool(len(deq))))
    elif act == "front":
        try:
            print(deq[0])
        except:
            print(-1)
    else:
        try:
            print(deq[-1])
        except:
            print(-1)
