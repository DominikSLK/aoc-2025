points = []

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        points.append([int(j) for j in i.split(",")])

max_area = 0

def area(x1, y1, x2, y2):
    xd = x1 - x2 + 1
    yd = y1 - y2 + 1
    return xd * yd

for i in range(len(points)):
    for j in range(len(points)):
        a = area(points[i][0], points[i][1], points[j][0], points[j][1])
        if a > max_area:
            max_area = a

print(max_area)