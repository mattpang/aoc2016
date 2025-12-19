codes = ["ULL", "RRDDD", "LURDL", "UUUUD"]

codes = open('inputs/2.txt').read().splitlines()


def run(part2=False):
    pad = dict()

    if not part2:
        pos = complex(1, 1)
        i = 1
        for x in range(3):
            for y in range(3):
                pad[complex(y, x)] = i
                i += 1
    else:
        pos = complex(0, 2)

        i = 1
        for y in range(0, 3):
            for x in range(2 - y, 2 + y + 1, 1):
                pad[complex(x, y)] = i
                i += 1
        pad[complex(1, 3)] = "A"
        pad[complex(2, 3)] = "B"
        pad[complex(3, 3)] = "C"
        pad[complex(2, 4)] = "D"

    code = ""
    for line in codes:
        for c in line:
            match c:
                case "U":
                    if pos + complex(0, -1) in pad.keys():
                        pos += complex(0, -1)
                case "R":
                    if pos + complex(1, 0) in pad.keys():
                        pos += complex(1, 0)
                case "D":
                    if pos + complex(0, 1) in pad.keys():
                        pos += complex(0, 1)
                case "L":
                    if pos + complex(-1, 0) in pad.keys():
                        pos += complex(-1, 0)

        code += str(pad[pos])

    print(code)


run()
run(True)
