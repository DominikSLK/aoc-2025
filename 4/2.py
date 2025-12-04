a = []
rolls = 0
positions = []

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        i = i.strip()
        a.append([t for t in i])

def get_or_none(i, j):
    if i < 0 or j < 0:
        return None
    try:
        return a[i][j]
    except:
        return None

def get_paper_count(i, j):
    c = 0
    e = [get_or_none(i-1, j), get_or_none(i-1, j+1), get_or_none(i-1, j-1), 
         get_or_none(i, j+1), get_or_none(i, j-1), 
         get_or_none(i+1, j), get_or_none(i+1, j+1), get_or_none(i+1, j-1)]
    for i in e:
        if i == "@":
            c += 1
    return c

def clean_accessible_rolls():
    global positions
    for i, r in enumerate(a):
        for j, t in enumerate(r):
            if [i, j] in positions:
                a[i][j] = "."
    positions = []

rr = -1
while rr > 0 or rr == -1:
    rr = 0
    for i, r in enumerate(a):
        for j, t in enumerate(r):
            if a[i][j] == "@":
                if get_paper_count(i, j) < 4:
                    positions.append([i, j])
                    rr += 1
                    rolls += 1
    clean_accessible_rolls()

print(rolls)