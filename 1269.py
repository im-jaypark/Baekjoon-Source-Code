a, b = map(int, input().split())
cnts = {}

for i in list(map(int, input().split())):
    cnts[i] = 1

for i in list(map(int, input().split())):
    try:
        if cnts[i] == 1:
            del cnts[i]
    except:
        cnts[i] = 1

print(len(cnts))
