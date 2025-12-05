ranges = []
good = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        if "-" in i:
            ranges.append([int(i.split("-")[0]), int(i.split("-")[1])])
        else:
            pass

def get_max_end(start):
    m = 0
    for i, r in enumerate(ranges):
        if r[0] == start:
            if r[1] > m:
                m = r[1]
    return m

ranges.sort(key=lambda x: x[0], reverse=True)

for i, r in enumerate(ranges):
    for ii, rr in enumerate(ranges):
        if rr[0] in range(r[0], r[1]+1):
            rr[0] = r[0]
            rr[1] = get_max_end(r[0])

u = set([(i[0], i[1]) for i in ranges])
for r in u:
    good += (r[1] - r[0]) + 1

print(good)