n = int(input())

for i in range(n):
    s = input()
    alters = [0, 0]
    pseudo = False

    if s == s[::-1]:
        print(0)
    else:
        for j in range(len(s) // 2):
            if s[j] != s[-j - 1]:
                if j == 0:
                    alters[0] = s[j + 1:]
                    alters[1] = s[:-j - 1]
                else:
                    alters[0] = s[:j] + s[j + 1:]
                    alters[1] = s[:-j - 1] + s[-j:]

                break

        for j in alters:
            if j == j[::-1]:
                pseudo = True
                print(1)
                break

        if not pseudo:
            print(2)
