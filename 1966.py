from collections import deque

for i in range(int(input())):
    n, m = map(int, input().split())
    ids = deque(range(n))
    values = deque(map(int, input().split()))

    while True:
        if values[0] == max(values):
            if ids[0] == m:
                print(n - len(ids) + 1)
                break
            ids.popleft()
            values.popleft()
        else:
            ids.append(ids.popleft())
            values.append(values.popleft())
