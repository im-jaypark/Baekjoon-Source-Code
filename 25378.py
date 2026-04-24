"""
MAX: N
MIN: ceil(N/2)

if a < b, a can't take more steps than b

For each location: you have 2 options
single, double

single: take all
why? if you don't take it all,
you'll eventually have to do single (which could have been done already)
or double (still 2 steps, but you can clear and remove the same amount in the
next one)

double: (NOT WHEN x1 > x2)
x1 < x2:
x1 = x2:

processes:

1. double chains
2. separate singles
3. separate doubles

Most efficient types (when a process clears a range)
1. separate doubles (N / 2)
2. double chains (N - 1)
3. separate singles (N)

each type clears an entire section: DP possible?

"""
N = int(input())
stones = list(map(int, input().split()))
dp = list(range(N + 1))

for i in range(1, N + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)

    if i >= 2 and stones[i - 1] == stones[i - 2]:
        dp[i] = min(dp[i], dp[i - 2] + 1)

    tempStones = stones[:i].copy()

    for j in range(i - 2, -1, -1):
        if tempStones[j] < tempStones[j + 1]:
            break
        elif tempStones[j] == tempStones[j + 1]:
            dp[i] = min(dp[i], dp[j] + i - j - 1)
            break
        else:
            tempStones[j] -= tempStones[j + 1]
            tempStones[j + 1] = 0

print(dp[N])
