limits = []

d = """5-8
0-2
4-7"""

d = open("inputs/20.txt").read()

for line in d.splitlines():
    a, b = map(int, line.split("-"))
    limits.append([a, b])

limits.sort()


def part1():
    bottom = 0
    old_bot = 0

    while True:
        for a, b in limits:
            if a <= bottom <= b:
                bottom = b + 1

        if old_bot == bottom:
            break
        old_bot = bottom

    print(bottom)

def overlap(a,b):

    if b[0]<=a[1] and b[1]>=a[1]:
        return [a[0],b[1]]
    else:
        return None

# limits = [[0,10],[5,15],[20,30]]
# limits.sort(reverse=True)

def part2():

    ip = 0
    i = 0
    total = 0
    while ip < 2**32:
        lower, upper = limits[i]
        if ip >= lower:
            if ip <= upper:
                ip = upper + 1
                continue
            i += 1
        else:
            total += 1
            ip += 1
    
    print(total)

part1()
part2()
