n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]
dfs = [v]
bfs = [v]

def search(x, method):
    global noPaths
    noPaths = True
    
    for i in graph[x]:
        if i not in method:
            method.append(i)
            noPaths = False
            break

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort()

allNoPaths = False

while allNoPaths == False: #DFS
    allNoPaths = True
    count = 0
    search(dfs[-1], dfs)
    
    while noPaths == True:
        try:
            count += 1
            search(dfs[-1 - count], dfs)
        except:
            break

    if noPaths == False:
        allNoPaths = False

count = 1
allNoPaths = False

while allNoPaths == False: # BFS
    allNoPaths = True
    toDo = bfs[len(bfs) - count - 1:]
    for i in toDo:
        for j in range(len(graph[i])):
            search(i, bfs)
            
            if noPaths == False:
                allNoPaths = False
            
    count = len(bfs) - count
    
print(*dfs)
print(*bfs)
