def dfs(pw, ind, vows):
    if len(pw) == l:
        print("".join(pw))
    else:
        for i in range(ind, c):
            if chars[i] in vowels:
                if len(pw) == l - 1:
                    if len(pw) - vows >= 2:
                        dfs(pw + [chars[i]], i + 1, vows + 1)
                elif len(pw) == l - 2:
                    if len(pw) - vows >= 1:
                        dfs(pw + [chars[i]], i + 1, vows + 1)
                else:
                    dfs(pw + [chars[i]], i + 1, vows + 1)
            else:
                if vows != 0 or len(pw) != l - 1:
                    dfs(pw + [chars[i]], i + 1, vows)

l, c = map(int, input().split())
chars = sorted(input().split())
vowels = ["a", "e", "i", "o", "u"]

dfs([], 0, 0)
