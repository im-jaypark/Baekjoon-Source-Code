n = int(input())
grades = list(map(int, input().split()))
lowest = grades[-1]
gradeSum = grades[-1]
maxGrade = max(grades[-2:])
bests = []

for i in range(2, n):
    lowest = min(lowest, grades[-i])
    gradeSum += grades[-i]
    grade = (gradeSum - lowest) / (i - 1)

    if grade > maxGrade:
        maxGrade = grade
        bests = [n - i]
    elif grade == maxGrade:
        bests.append(n - i)

for i in bests[::-1]:
    print(i)
