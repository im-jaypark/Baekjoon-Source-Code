n = int(input())
methods = [1, 2]

for i in range(n - 2):
    methods.append((methods[-1] + methods[-2]) % 15746)

print(methods[n - 1] % 15746)
