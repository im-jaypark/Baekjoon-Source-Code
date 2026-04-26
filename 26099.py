n = int(input())
temp = n % 5

while temp % 3 != 0:
    temp += 5

if temp > n:
    print(-1)
else:
    print(temp // 3 + (n - temp) // 5)
