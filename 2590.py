sqrs = [int(input()) for i in range(6)]
threes = [0, 5, 3, 1, 0]
areas = [0, 27, 18, 9, 0]
count = 0
temp = [0, 0]

while True:
    count += 1
    
    if sqrs[5] > 0:
        sqrs[5] -= 1
    elif sqrs[4] > 0:
        sqrs[4] -= 1
        sqrs[0] -= min(sqrs[0], 11)
    elif sqrs[3] > 0:
        temp[0] = min(sqrs[1], 5)
        
        sqrs[3] -= 1
        sqrs[1] -= temp[0]
        sqrs[0] -= min(sqrs[0], 4 * (5 - temp[0]))
    elif sqrs[2] > 0:
        temp[0] = min(sqrs[2], 4)
        temp[1] = min(sqrs[1], threes[temp[0]])
                      
        sqrs[2] -= temp[0]
        sqrs[1] -= temp[1]
        sqrs[0] -= min(sqrs[0], areas[temp[0]] - 4 * temp[1])
    elif sqrs[1] > 0:
        temp[0] = min(sqrs[1], 9)

        sqrs[1] -= temp[0]
        sqrs[0] -= min(sqrs[0], 36 - 4 * temp[0])
    elif sqrs[0] > 0:
        sqrs[0] -= min(sqrs[0], 36)
    else:
        break

print(count - 1)
