from collections import Counter


def decoy(x) -> bool:
    pos = x.find("[")
    c = Counter()
    for chunk in x[:pos].split("-"):
        if not chunk.isdigit():
            for a in chunk:
                c[a] += 1
    sector_id = int(chunk)
    code = x[pos + 1 : -1]
    x = c.most_common()

    x = sorted(sorted(x, key=lambda x: x[0]), key=lambda x: x[1], reverse=True)

    return code == "".join([i[0] for i in x])[0 : len(code)], sector_id


assert decoy("aaaaa-bbb-z-y-x-123[abxyz]")[0] is True
assert decoy("a-b-c-d-e-f-g-h-987[abcde]")[0] is True
assert decoy("not-a-real-room-404[oarel]")[0] is True
assert decoy("totally-real-room-200[decoy]")[0] is False

d = open("inputs/4.txt").read()

tally = 0
for line in d.splitlines():
    result, id = decoy(line)
    if result:
        tally += id
print(tally)

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def decyrpt(x) -> str:
    pos = x.find("[")
    c = Counter()
    chunks = x[:pos].split("-")
    string = x[:pos-4].replace('-',' ').upper()
    
    shift = int(chunks[-1])
    print(string)
    new_string = ''
    for c in string:
        if c in alpha:
            new_string+=alpha[(alpha.index(c) + shift) % 26]
        else:
            new_string+=' '
    return new_string


print(decyrpt("qzmt-zixmtkozy-ivhz-343"))
