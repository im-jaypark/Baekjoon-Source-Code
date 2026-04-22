def alToNum(x):
    if x == ".":
        return -1
    
    return alphabet.index(x)

def search(node, type):
    if type == 0:
        path.append(alphabet[node])
    if tree[node][0] != ".":
        search(tree[node][0], type)
    if type == 1:
        path.append(alphabet[node])
    if tree[node][1] != ".":
        search(tree[node][1], type)
    if type == 2:
        path.append(alphabet[node])

N = int(input())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tree = [["."] * 2 for i in range(N)]

for i in range(N):
    p, l, r = map(alToNum, input().split())
    
    for j in range(2):
        if (l, r)[j] != -1:
            tree[p][j] = (l, r)[j]

for i in range(3):
    path = []
    search(0, i)
    print("".join(path))
