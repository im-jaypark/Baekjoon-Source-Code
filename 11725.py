import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

def dfs(node):
    visited[node] = True
    
    for i in tree[node]:
        if not visited[i]:
            parents[i] = node
            dfs(i)

N = int(input())
tree = [[] for i in range(N + 1)]
parents = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)

for i in range(2, N + 1):
    print(parents[i])
