split = 0
a = []

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        a.append([j for j in i])

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i-1][j] == "S":
            a[i][j] = "|"
        elif a[i][j] == "^" and a[i-1][j] == "|":
            a[i][j-1] = "|"
            a[i][j+1] = "|"
            split += 1
        elif a[i-1][j] == "|":
            a[i][j] = "|"

print(split)