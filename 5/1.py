ranges = []
ingredients = []
good = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        if "-" in i:
            ranges.append([int(i.split("-")[0]), int(i.split("-")[1])])
        elif i == "":
            pass
        else:
            ingredients.append(int(i))

def is_good(ingredient):
    a = False
    for r in ranges:
        a = ingredient in range(r[0], r[1]+1)
        if a == True:
            break
    return a

for i in ingredients:
    if is_good(i):
        good += 1

print(good)