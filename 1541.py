equation = list(input())
inParentheses = False

if "-" not in equation:
    print(eval("".join(equation)))
else:
    for i in range(len(equation)):
        try:
            while i == 0 or equation[i - 1] in ("+", "-"):
                if equation[i] == "0":
                    del equation[i]
                else:
                    break
        except:
            if i > len(equation):
                break
        
    for i in range(len(equation) + equation.count("-") * 2 - 1):
        if equation[i] == "-":
            if inParentheses == False:
                equation.insert(i + 1, "(")
                inParentheses = True
            else:
                equation.insert(i, ")")
                inParentheses = False
        if i == len(equation) - 1 and inParentheses == True:
            equation.append(")")

    print(eval("".join(equation)))
