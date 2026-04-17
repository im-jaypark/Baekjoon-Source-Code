n = int(input())
primes = [0] * 2 + [1] * max(n - 1, 1)

for i in range(2, int(n ** 0.5) + 1):
    if primes[i] == 1:
        for j in range(i ** 2, n + 1, i):
            primes[j] = 0

primes = [i for i in range(2, max(n + 1, 3)) if primes[i] == 1]
sums = 0
start = 0
end = 0
consecSum = 2

while end >= start:
    if consecSum < n and end < len(primes) - 1:
        end += 1
        consecSum += primes[end]
    else:
        if consecSum == n:
            sums += 1

        start += 1
        consecSum -= primes[start - 1]

print(sums)
