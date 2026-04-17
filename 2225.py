import math

n, k = map(int, input().split())
x = 1

for i in range(n):
    x *= k + i

print(x // math.factorial(n) % 10 ** 9)
