N = int(input())
A = input()
B = input()
p1, p3, p5, ppair = map(int, input().split())
totalDP = [float("inf")] * N

for i in range(N):
    aDP = [0] * (i + 6)
    bDP = [0] * (i + 6)

    if i < 4:
        totalDP[i] = ppair
    else:
        totalDP[i] = totalDP[i - 4] + ppair

    for j in range(i, -1, -1):
        if A[j] == "1":
            aDP[j] = min(aDP[j + 1] + p1, aDP[j + 3] + p3, aDP[j + 5] + p5)
        else:
            aDP[j] = aDP[j + 1]

        if B[j] == "1":
            bDP[j] = min(bDP[j + 1] + p1, bDP[j + 3] + p3, bDP[j + 5] + p5)
        else:
            bDP[j] = bDP[j + 1]

        if j == 0:
            totalDP[i] = min(totalDP[i], aDP[j] + bDP[j])
        else:
            totalDP[i] = min(totalDP[i], totalDP[j - 1] + aDP[j] + bDP[j])

print(totalDP[-1])
"""
for i in range(N):
    if i >= 4:
        together = totalDP[i - 4] + ppair
    else:
        together = ppair

    totalDP = min("""
"""
Q: Can there be a descending part in aDP or bDP?
A: NO. You can buy the tickets before the trip.

Q: Is there a need to have a ticket expire after the trip?
A:

Q: Do you need to buy tickets when you have 1 in use?
A: Individual: No. Together: Not if DP is always sorted

Each DP item will show the minimum cost to complete X days and have the ticket
expire there. So you have to buy a new one the next day.

Q: can I add from the previous totalDP for each a and b?

for each item in DP:
1. assume that all previous items in DP are optimal
2.


why a1 and b1 strat works:
- assume DP has the last pp
- if someone in a1+b1 has pp, then the DP until that should have that
an
"""
