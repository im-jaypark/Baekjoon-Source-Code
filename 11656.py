s = input()
pres = []

for i in range(len(s)):
    pres.append(s[i:])

for i in sorted(pres):
    print(i)
