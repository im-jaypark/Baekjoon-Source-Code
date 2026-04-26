n, q = map(int, input().split())
count = 0

xy = [[n for i in range(n)] for i in range(n)]
xz = [[n for i in range(n)] for i in range(n)]
yz = [[n for i in range(n)] for i in range(n)]

for i in range(q):
    x, y, z = map(int, input().split())
    
    xy[x][y] -= 1
    xz[x][z] -= 1
    yz[y][z] -= 1

    if xy[x][y] == 0:
        count += 1
    
    if xz[x][z] == 0:
        count += 1
    
    if yz[y][z] == 0:
        count += 1

    print(count)
