n, l = map(int, input().split())
holes = sorted(list(map(int, input().split())))
n = len(holes)
clear = [0] * n
tapes = 0

for i in range(n):
    if clear[i] == 0:
        for j in range(1, min(l, n - i)):
            if holes[i + j] - holes[i] < l:
                clear[i + j] = 1

        clear[i] = 1
        tapes += 1

print(tapes)
