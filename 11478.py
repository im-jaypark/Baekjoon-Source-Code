s = input()
n = len(s)
segs = set()

for i in range(1, n + 1):
    for j in range(n - i + 1):
        segs.add(s[j:j + i])

print(len(segs))
