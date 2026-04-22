import math

a, b, c = map(int, input().split())
print(pow(a, b, c))
"""
# solution prototype.1
a, b, c = map(int, input().split())
n = int(b ** 0.5)
k = b - n ** 2

print(a ** k * (a ** n) ** n % c)

# solution prototype.2
def power(b):
    if b == 1:
        return a
    elif b % 2 == 0:
        return power(b // 2) ** 2
    else:
        return a * power((b - 1) // 2) ** 2

a, b, c = map(int, input().split())
print(power(b) % c)
"""
