a = []
total = 0
b = []
c = []

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.replace("\n", "")
        e = [i for i in i.split(" ") if i != ""]
        b.append(i)
        c.append(e)

max_lens = []
for i in range(len(c[0])):
    n = []
    for j in range(len(c)):
        n.append(len(c[j][i]))
    max_lens.append(max(n))

for i in b:
    x = []
    t = 0
    for j in max_lens:
        x.append(i[t:t+j])
        t += j+1
    a.append(x)

for i in range(len(a[0])):
    s = 0
    n = []
    for j in range(len(a)):
        n.append(a[j][i])

    m = max([len(a) for a in n])
    real_numbers = []

    for e in range(m):
        real_numbers.append("")
        for ee in range(len(n)-1):
            real_numbers[e] += n[ee][e]

    for j in real_numbers:
        try:
            if "*" in n[-1]:
                if s == 0:
                    s = 1
                s *= int(j)
            elif "+" in n[-1]:
                s += int(j)
        except:
            pass
    total += s

print(total)