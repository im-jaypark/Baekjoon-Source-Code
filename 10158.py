w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
tx = t % (2 * w)
ty = t % (2 * h)

if x + tx > w:
    x = (2 * w) - x - tx

    if x < 0:
        x *= -1
else:
    x += tx

if y + ty > h:
    y = (2 * h) - y - ty

    if y < 0:
        y *= -1
else:
    y += ty

print(x, y)
