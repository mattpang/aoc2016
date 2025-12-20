from collections import Counter, defaultdict


pos_count = defaultdict(Counter)

d = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

d = open("inputs/6.txt").read()

for line in d.splitlines():
    for i, c in enumerate(line):
        pos_count[i][c] += 1

out = ""
for i in range(len(d.splitlines()[0])):
    out += pos_count[i].most_common(1)[0][0]
print(out)

out = ""
for i in range(len(d.splitlines()[0])):
    out += pos_count[i].most_common()[-1][0]
print(out)
