n = int(input())
methods = [1, 1]

for i in range(n - 1):
    methods.append(methods[-1] + methods[-2])

print(methods[n] % 10007)
