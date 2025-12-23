from collections import Counter
import math


d = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""

d = open("inputs/23.txt").read()

lines = d.splitlines()


def sim(part2=False):
    pos = 0
    reg = Counter()
    if part2:
        reg["a"] = 12
    else:
        reg["a"] = 7

    reg["b"] = 0
    reg["c"] = 0
    reg["d"] = 0

    while True:
        if pos < 0 or pos > len(lines) - 1:
            break

        line = lines[pos]
        # print(line)

        parts = line.split()
        match parts[0]:
            case "cpy":
                if parts[2].isdigit():
                    pos += 1
                    print("invalid line, skipping")
                    print(line)
                    continue
                if parts[1] in "abcd":
                    reg[parts[2]] = reg[parts[1]]
                else:
                    reg[parts[2]] = int(parts[1])
            case "inc":
                reg[parts[1]] += 1
            case "dec":
                reg[parts[1]] -= 1
            case "jnz":
                if parts[2] in "abcd":
                    val = reg[parts[2]]
                else:
                    val = int(parts[2])
                # print(f"{line=}, {pos=}, {parts[2]=}, {val=}, {reg=}")

                # print(line,reg[parts[1]],val)
                if parts[1].isdigit():
                    if parts[1] != "0":
                        pos += val
                        continue
                elif reg[parts[1]] != 0:
                    pos += val
                    continue

            case "tgl":
                # toggle
                # For one-argument instructions, inc becomes dec, and all other one-argument instructions become inc.
                # For two-argument instructions, jnz becomes cpy, and all other two-instructions become jnz.
                if parts[1] in "abcd":
                    op_val = reg[parts[1]]
                else:
                    op_val = int(parts[1])
                try:
                    future = lines[pos + op_val]
                except IndexError:
                    pos += 1
                    continue
                if len(future.split()) == 3:
                    if "jnz" in future:
                        lines[pos + op_val] = "cpy" + future[3:]
                    else:
                        lines[pos + op_val] = "jnz" + future[3:]

                elif len(future.split()) == 2:
                    if "inc" in future:
                        lines[pos + op_val] = "dec" + future[3:]
                    else:
                        lines[pos + op_val] = "inc" + future[3:]

        pos += 1

    print(reg["a"])


sim(part2=False)
# sim(part2=True)
# print(77*73+12)
print(math.factorial(12) + 77 * 73)
