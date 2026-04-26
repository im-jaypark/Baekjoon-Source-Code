n = int(input())
infos = []

for i in range(n):
    name, kor, eng, math = input().split()
    kor, eng, math = list(map(int, [kor, eng, math]))
    infos.append((-kor, eng, -math, name))

infos.sort()

for i in infos:
    print(i[3])
