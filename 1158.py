n, k = map(int, input().split())
q = list(range(1, n + 1))
eli = []

for i in range(n):
    temp = (k - 1) % len(q)
    eli.append(q.pop(temp))
    q = q[temp:] + q[:temp]

print("<" + str(eli)[1:-1] + ">")
