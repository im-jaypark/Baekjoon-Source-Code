n = int(input())
count = 0
fstAlph = [0] * 26
abcs = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
            "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14,
            "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21,
            "W": 22, "X": 23, "Y": 24, "Z": 25}

for i in input():
    fstAlph[abcs[i]] += 1

for i in range(n - 1):
    alph = [0] * 26
    subbed = 0
    added = 0
    diff = False

    for j in input():
        alph[abcs[j]] += 1

    for j in range(26):
        if alph[j] != fstAlph[j]: 
            if alph[j] - fstAlph[j] == -1:
                if subbed < 1:
                    subbed += 1
                else:
                    diff = True
                    break
            elif alph[j] - fstAlph[j] == 1:
                if added < 1:
                    added += 1
                else:
                    diff = True
                    break
            else:
                diff = True
                break

    if not diff:
        count += 1

print(count)
