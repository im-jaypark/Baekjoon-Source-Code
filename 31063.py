n, m = map(int, input().split())

cowHeights = list(map(int, input().split()))
caneHeights = list(map(int, input().split()))
caneBases = [0 for i in range(m)]

for i in range(m):
    for j in range(n):
        if caneHeights[i] > caneBases[i]:
            if cowHeights[j] > caneBases[i]:
                eaten = min(cowHeights[j], caneHeights[i]) - caneBases[i]
                cowHeights[j] += eaten
                caneBases[i] += eaten
        else:
            break

for i in cowHeights:
    print(i)
