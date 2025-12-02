
total = 0

def get_parts(number, count):
    parts = []
    part_len = count
    for i in range(len(number)//count):
        parts.append(number[i*part_len:(i+1)*part_len])

    return parts

def check_repeat(number):
    aa = False
    for i in range(1, len(number)//2+1):
        parts = get_parts(number, i)
        a = {}
        for p in parts:
            if p in a:
                a[p] += 1
            else:
                a[p] = 1
        for k, v in a.items():
            if v > 1:
                if len(a) == 1:
                    if number.replace(k, "") == "":
                        aa = True
                else:
                    pass
        
    return True if aa > 0 else False

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.read().replace("\n", "").split(","):
        start = i.split("-")[0]
        stop = i.split("-")[1]
        for i in range(int(start), int(stop)+1):
            if check_repeat(str(i)):
                total += i

print(total)