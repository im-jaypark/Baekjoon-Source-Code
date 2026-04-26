def minClock(clock):
    clocks = [clock[i:] + clock[:i] for i in range(4)]
    return min(clocks)

myClock = minClock("".join(input().split()))
distinctClocks = 0

for i in range(1111, 10000):
    if "0" not in str(i):
        if minClock(str(i)) == str(i):
            distinctClocks += 1

            if str(i) == myClock:
                break

print(distinctClocks)
