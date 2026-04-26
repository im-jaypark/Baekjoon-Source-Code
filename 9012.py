n = int(input())
balance = 0

for i in range(n):
    pars = list(input())
    isVps = 1
    balance = 0
    
    for par in pars:
        if par == "(":
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            isVps = 0
            break

    if balance != 0:
        isVps = 0

    if isVps == 1:
        print("YES")
    else:
        print("NO")
