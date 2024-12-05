from math import sqrt

with open('circle.txt') as f:
    xc, yc = map(float, f.readline().split())
    r = int(f.readline())

with open('dot.txt') as f:
    points = f.readlines()

for point in points:
    x, y = map(float, point.split())
    s = sqrt((xc - x) ** 2 + (yc - y) ** 2)
    if s == r:
        print(0)
    elif s < r:
        print(1)
    else:
        print(2)