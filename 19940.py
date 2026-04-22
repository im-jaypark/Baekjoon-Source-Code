T = int(input())

for i in range(T):
    N = int(input())
    remainder = N % 60
    clicks = [0] * 5
    clicks[0] = N // 60
    candidates = [clicks.copy() for i in range(4)]

    candidates[0][1] += remainder // 10
    candidates[0][3] += remainder % 10

    candidates[1][1] += remainder // 10 + 1
    candidates[1][4] += 10 - remainder % 10

    candidates[2][0] += 1
    candidates[2][2] += 6 - remainder // 10
    candidates[2][3] += remainder % 10

    candidates[3][0] += 1
    candidates[3][2] += 6 - remainder // 10 - 1
    candidates[3][4] += 10 - remainder % 10

    candidates.sort()
    totals = [sum(i) for i in candidates]
    print(*candidates[totals.index(min(totals))])

"""
Every 60 minutes: faster with ADDH

1. Start from 0
1a. go to N // 10 * 10, climb up (1, 3)
1b. go to N // 10 * 10 + 10, climb down (1, 4)

2. Start from 60
2a. go to N // 10 * 10, climb up (2, 3)
2b. go to N // 10 * 10 + 10, climb down (2, 4)
"""
