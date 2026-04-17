s1 = input()
s2 = input()
lcsStrs = [[""] * (len(s2) + 1) for i in range(len(s1) + 1)]

for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            lcsStrs[i][j] = lcsStrs[i - 1][j - 1] + s1[i - 1]

        for k in ((-1, 0), (0, -1)):
            if len(lcsStrs[i + k[0]][j + k[1]]) > len(lcsStrs[i][j]):
                lcsStrs[i][j] = lcsStrs[i + k[0]][j + k[1]]

print(len(lcsStrs[len(s1)][len(s2)]))
print(lcsStrs[len(s1)][len(s2)])
