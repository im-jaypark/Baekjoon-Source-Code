points = []

for i in range(3):
    points.append(list(map(int, input().split())))

slope = [points[1][1] - points[0][1], points[1][0] - points[0][0]]

if slope[1] == 0:
    direction = 2 * int(points[1][1] > points[0][1]) - 1

    if points[2][0] > points[0][0]:
        print(direction * -1)
    elif points[2][0] == points[0][0]:
        print(0)
    else:
        print(direction * 1)
else:
    direction = 2 * int(points[1][0] > points[0][0]) - 1
    expected = (points[2][0] - points[0][0]) * slope[0] / slope[1] + points[0][1]

    if points[2][1] > expected:
        print(direction * 1)
    elif points[2][1] == expected:
        print(0)
    else:
        print(direction * -1)
