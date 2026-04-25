N, K = map(int, input().split())
line = list(input())
taken = [False] * N
happyPeople = 0

for i in range(N):
    if line[i] == "P":
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if line[j] == "H" and not taken[j]:
                taken[j] = True
                happyPeople += 1
                break

print(happyPeople)
