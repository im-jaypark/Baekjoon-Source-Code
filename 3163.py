from collections import deque

T = int(input())

for i in range(T):
    N, L, k = map(int, input().split())
    leftTimes = deque()
    rightTimes = deque()
    ants = deque()

    for j in range(N):
        pos, ant = map(int, input().split())

        if ant > 0:
            rightTimes.appendleft(L - pos)
        else:
            leftTimes.append(pos)

        ants.append(ant)

    for j in range(k):
        if leftTimes and rightTimes:
            if leftTimes[0] < rightTimes[0]:
                leftTimes.popleft()
                currentAnt = ants.popleft()
            elif leftTimes[0] > rightTimes[0]:
                rightTimes.popleft()
                currentAnt = ants.pop()
            elif ants[0] < ants[-1]:
                leftTimes.popleft()
                currentAnt = ants.popleft()
            else:
                rightTimes.popleft()
                currentAnt = ants.pop()
        elif leftTimes:
            leftTimes.popleft()
            currentAnt = ants.popleft()
        else:
            rightTimes.popleft()
            currentAnt = ants.pop()

    print(currentAnt)
