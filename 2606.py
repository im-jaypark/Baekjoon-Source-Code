def search(n):
    visited[n] = True
    infected.append(n)

    for i in paths[n]:
        if not visited[i]:
            search(i)

computers = int(input())
paths = [[] for i in range(computers + 1)]
infected = []
visited = [False for i in range(computers + 1)]

for i in range(int(input())):
    n, m = map(int, input().split())
    
    paths[n].append(m)
    paths[m].append(n)

search(1)

print(len(infected) - 1)
