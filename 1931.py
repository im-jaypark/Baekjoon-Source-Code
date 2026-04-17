n = int(input())
meetings = []
maxMeetings = 0
time = 0

for i in range(n):
    meetings.append(list(map(int, input().split()))[::-1])

meetings.sort()

for i in meetings:
    if i[1] >= time:
        time = i[0]
        maxMeetings += 1

print(maxMeetings)
