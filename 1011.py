for i in range(int(input())):
    x, y = map(int, input().split())
    diff = y - x
    count = 0
    temp = 0

    while temp < diff:
        count += 1
        
        temp += (count - 1) // 2

    print(count - 2)
