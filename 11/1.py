paths = {}
total = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        paths[i.split(": ")[0]] = i.split(": ")[1].split(" ")

def go_path(p):
    global total
    if p == "out":
        total += 1
        return
    for i in paths[p]:
        go_path(i)

go_path("you")
print(total)