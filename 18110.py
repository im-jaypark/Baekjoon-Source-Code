n = int(input())
scores = []

if n == 0:
    print(0)
else:
    for i in range(n):
        scores.append(int(input()))

    scores.sort()
    cut = int(0.15 * n + 0.5)
    scores = scores[cut:n - cut]
    
    print(int(sum(scores) / len(scores) + 0.5))
