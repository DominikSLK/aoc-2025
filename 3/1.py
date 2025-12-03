banks = []
total = 0

def get_all_possible(n, bank):
    all = []

    for i in bank:
        all.append(n + i)

    return all

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        banks.append(i)

for b in banks:
    possible = []
    for i, a in enumerate(b):
        a = [int(i) for i in get_all_possible(a, b[i+1:])]
        a.sort(reverse=True)
        if len(a) > 0:
            possible.append(a[0])

    possible.sort(reverse=True)
    total += possible[0]

print(total)
