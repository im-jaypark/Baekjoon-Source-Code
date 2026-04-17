n = int(input())
crosses = list(map(int, input().split()))
direction = 1
change = {1: "R", -1: "L"}
pos = 0
moves = []

while crosses[0] != 0:
    if direction == 1:
        if pos == n:
            direction = -1
        elif crosses[pos] == 0:
            direction = -1
        else:
            crosses[pos] -= 1
            moves.append(change[direction])
            pos += 1
    else:
        if pos == 0:
            direction = 1
        elif crosses[pos - 1] == 1:
            if pos == n or crosses[pos] == 0:
                crosses[pos - 1] -= 1
                moves.append(change[direction])
                pos -= 1
            else:
                direction = 1
        else:
            crosses[pos - 1] -= 1
            moves.append(change[direction])
            pos -= 1

print("".join(moves))
