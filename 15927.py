word = input()

if word == word[::-1]:
    if word[:-1] == word[:-1][::-1]:
        print(-1)
    else:
        print(len(word) - 1)
else:
    print(len(word))
