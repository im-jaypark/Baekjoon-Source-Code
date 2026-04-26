n = int(input())
binary = 1

while True:
    if binary >= n:
        break
    else:
        binary *= 2

print(binary - 2 * (binary - n))
