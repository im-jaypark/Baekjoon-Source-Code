from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001
visited[n] = True
path = deque([[n]])
broken = False
count = 0

if n == k:
    print(0)
elif n > k:
    print(n - k)
else:
    while True:
        path.append([])
        count += 1

        for i in path[-2]:
            toCheck = [i - 1, i + 1, 2 * i]
            for j in toCheck:
                if 0 <= j <= 100000 and not visited[j]:
                    path[-1].append(j)
                    visited[j] = True

                if j == k:
                    broken = True
                    break

            if broken:
                break

        if broken:
            break

        path.popleft()

    print(count)
