n = int(input())
times = sorted(list(map(int, input().split())))
ans = 0

for i in range(1, n + 1):
    ans += sum(times[:i])

print(ans)
