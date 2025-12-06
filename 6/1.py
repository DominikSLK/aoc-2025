a = []
total = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        a.append([i for i in i.split(" ") if i != ""])

for i in range(len(a[0])):
    s = 0
    for j in range(len(a)):
        if a[j][i] not in ("*", "+"):
            if a[-1][i] == "*":
                if s == 0:
                    s = 1
                s *= int(a[j][i])
            elif a[-1][i] == "+":
                s += int(a[j][i])
    total += s

print(total)