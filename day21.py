# swap position X with position Y means that the letters at indexes X and Y (counting from 0) should be swapped.
# swap letter X with letter Y means that the letters X and Y should be swapped (regardless of where they appear in the string).
# rotate left/right X steps means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
# rotate based on position of letter X means that the whole string should be rotated to the right based on the index of letter X (counting from 0) as determined before this instruction does any rotations. Once the index is determined, rotate the string to the right one time, plus a number of times equal to that index, plus one additional time if the index was at least 4.
# reverse positions X through Y means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
# move position X to position Y means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
import copy
from collections import deque

d = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d"""


def part1(ans="abcdefgh"):
    d = open("inputs/21.txt").read()

    code = list(ans)

    for line in d.splitlines():
        parts = line.split()

        this_code = copy.deepcopy(code)

        if parts[0] == "swap" and parts[1] == "position":
            this_code[int(parts[2])] = code[int(parts[5])]
            this_code[int(parts[5])] = code[int(parts[2])]
        elif parts[0] == "swap" and parts[1] == "letter":
            pos_x = code.index(parts[2])
            pos_y = code.index(parts[5])

            this_code[pos_x] = code[pos_y]
            this_code[pos_y] = code[pos_x]
        elif parts[0] == "reverse":
            this_code[int(parts[2]) : int(parts[4]) + 1] = code[
                int(parts[2]) : int(parts[4]) + 1
            ][::-1]
        elif parts[0] == "move":
            X = code[int(parts[2])]
            del code[int(parts[2])]
            code.insert(int(parts[5]), X)

            this_code = copy.deepcopy(code)
        elif parts[0] == "rotate" and parts[1] == "left":
            d = deque(code)
            d.rotate(-int(parts[2]))
            this_code = list(d)
        elif parts[0] == "rotate" and parts[1] == "right":
            d = deque(code)
            d.rotate(int(parts[2]))
            this_code = list(d)

        elif parts[0] == "rotate" and parts[1] == "based":
            pos_x = code.index(parts[6])
            rot = pos_x + 1
            if pos_x >= 4:
                rot += 1
            d = deque(code)
            d.rotate(rot)

            this_code = list(d)

        code = this_code

    return "".join(this_code)


print(part1())

from itertools import permutations


for p in permutations('fbgdceah',8):
    if part1(p) == 'fbgdceah':
        print("".join(p))
        break