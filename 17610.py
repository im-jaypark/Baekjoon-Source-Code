board = input().split(".")
ans = []
possible = 1

for i in board:
    if len(i) % 2 == 0:
        ans.append("AAAA" * (len(i) // 4) + "BB" * ((len(i) % 4) // 2))
    else:
        possible = 0

if possible:
    print(".".join(ans))
else:
    print(-1)
