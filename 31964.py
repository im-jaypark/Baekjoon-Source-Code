n = int(input())
x = list(map(int, input().split()))
t = list(map(int, input().split()))
mgcNum = 2 * x[-1]
lags = [max(t[i] - mgcNum + x[i], 0) for i in range(n)]

print(mgcNum + max(lags))
