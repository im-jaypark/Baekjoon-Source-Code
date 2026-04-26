while True:
    text = input()
    parenStack = []
    error = False

    if text == ".":
        break

    for i in text:
        if i in ["(", "["]:
            parenStack.append(i)
        elif i == ")":
            if parenStack and parenStack[-1] == "(":
                parenStack.pop()
            else:
                error = True
                break
        elif i == "]":
            if parenStack and parenStack[-1] == "[":
                parenStack.pop()
            else:
                error = True
                break

    if parenStack:
        error = True

    if error:
        print("no")
    else:
        print("yes")
