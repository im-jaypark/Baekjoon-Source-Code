n = int(input())
cows = [[0, "Bessie"], [0, "Elsie"], [0, "Daisy"], [0, "Gertie"],
        [0, "Annabelle"], [0, "Maggie"], [0, "Henrietta"]]
cowNames = {"Bessie": 0, "Elsie": 1, "Daisy": 2, "Gertie": 3,
            "Annabelle": 4, "Maggie": 5, "Henrietta": 6,}

for i in range(n):
    a, b = input().split()
    cows[cowNames[a]][0] += int(b)

cows.sort()
last = cows[0][0]
found = False

for i in range(1, 7):
    if cows[i][0] != last:
        found = True
        if i != 6:
            if cows[i][0] == cows[i + 1][0]:
                print("Tie")    
            else:
                print(cows[i][1])

            break
        else:
            print(cows[i][1])
            break

if not found:
    print("Tie")
