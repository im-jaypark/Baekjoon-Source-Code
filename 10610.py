n = sorted([int(i) for i in input()], reverse=True)

if n[-1] == 0 and sum(n) % 3 == 0:
    print("".join(str(i) for i in n))
else:
    print(-1)
