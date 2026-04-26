n = int(input())
queue = []

for i in range(n):
    command = list(input().split())

    if len(command) == 2:
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if queue == []:
            print(-1)
        else:
            print(queue.pop(0))
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        if queue == []:
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if queue == []:
            print(-1)
        else:
            print(queue[0])
    else:
        if queue == []:
            print(-1)
        else:
            print(queue[-1])
