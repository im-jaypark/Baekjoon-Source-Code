import math

a, b = map(int, input().split())
c, d = map(int, input().split())
den = math.lcm(b, d)
num = den // b * a + den // d * c
temp = math.gcd(den, num)
den //= temp
num //= temp

print(num, den)
