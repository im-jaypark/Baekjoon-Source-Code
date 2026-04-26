n, m = map(int, input().split())
numName = [0]
nameNum = {}

for i in range(1, n + 1):
    pokemon = input()
    numName.append(pokemon)
    nameNum[pokemon] = i

for i in range(m):
    isNum = True
    quiz = input()

    try:
        quiz = int(quiz)
    except:
        isNum = False

    if isNum:
        print(numName[quiz])
    else:
        print(nameNum[quiz])
