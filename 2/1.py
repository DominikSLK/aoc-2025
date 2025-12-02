
total = 0

def check_repeat(number):
    part1 = number[0:len(number)//2]
    part2 = number[len(number)//2:]
    if part1 == part2:
        return True

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f.read().replace("\n", "").split(","):
        start = i.split("-")[0]
        stop = i.split("-")[1]
        for i in range(int(start), int(stop)+1):
            if check_repeat(str(i)):
                total += i

print(total)