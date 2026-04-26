n, k = map(int, input().split())
cashTypes = []
count = 0

for i in range(n):
    cashType = int(input())

    if cashType <= k:
        cashTypes.append(cashType)
    else:
        break

for cash in reversed(cashTypes):
    count += k // cash
    k %= cash

    if k == 0:
        break

print(count)
