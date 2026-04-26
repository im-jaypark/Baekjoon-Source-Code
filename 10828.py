n = int(input())
nums = []

for i in range(n):
    command = input()

    if "push" in command:
        nums.append(list(command.split())[-1])
    elif command == "pop":
        try:
            print(nums.pop(-1))
        except:
            print(-1)
    elif command == "size":
        print(len(nums))
    elif command == "empty":
        if nums == []:
            print(1)
        else:
            print(0)
    else:
        try:
            print(nums[-1])
        except:
            print(-1)
