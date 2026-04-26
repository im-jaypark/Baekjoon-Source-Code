n, m = map(int, input().split())
passwords = {}

for i in range(n):
    password = input().split()
    passwords[password[0]] = password[1]

for i in range(m):
    print(passwords[input()])
