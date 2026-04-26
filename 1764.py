n, m = map(int, input().split())
hearers = {}
strangers = []

for i in range(n):
    hearers[input()] = 0

for i in range(m):
    name = input()
    
    try:
        hearers[name] += 0
        strangers.append(name)
    except:
        pass

strangers.sort()
print(len(strangers))

for i in strangers:
    print(i)
