dial = 50
points_at_zero = 0

def add():
    global dial
    if dial == 99:
        dial = 0
    else:
        dial += 1

def remove():
    global dial
    if dial == 0:
        dial = 99
    else:
        dial -= 1

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        d = i[0]
        n = int(i[1:])
        if d == "L":
            for i in range(n):
                add()
        else:
            for i in range(n):
                remove()
        if dial == 0:
            points_at_zero += 1

print(points_at_zero)