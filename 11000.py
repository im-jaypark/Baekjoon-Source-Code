import heapq

N = int(input())
lectures = [list(map(int, input().split())) for i in range(N)] # [s, t]
heapq.heapify(lectures)
roomVacancies = []

for i in range(N):
    lecture = heapq.heappop(lectures) # [s, t]

    if roomVacancies and lecture[0] >= roomVacancies[0]:
        heapq.heapreplace(roomVacancies, lecture[1])
    else:
        heapq.heappush(roomVacancies, lecture[1])

print(len(roomVacancies))
