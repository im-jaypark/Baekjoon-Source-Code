from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    direction = 1
    p = input()[:-1]
    n = int(input())
    nums = deque(list(map(int, input()[:-1].replace(",", " ")[1:-1].split())))

    try:
        for j in p:
            if j == "R":
                direction *= -1
            else:
                if direction == 1:
                    deque.popleft(nums)
                else:
                    deque.pop(nums)

        print(str(list(nums)[::direction]).replace(" ", ""))
    except:
        print("error")
