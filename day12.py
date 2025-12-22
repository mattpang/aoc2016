
from collections import Counter



d = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

d = open('inputs/12.txt').read()

lines = d.splitlines()

def sim(pt2=False):
    
    pos = 0 
    reg = Counter()
    if pt2:
        reg['c'] = 1

    while True:

        if pos<0 or pos>len(lines)-1:
            break

        line = lines[pos]
        
        parts = line.split()
        match parts[0]:
            case "cpy":
                if parts[1].isdigit():
                    reg[parts[2]] = int(parts[1])
                else:
                    reg[parts[2]] = reg[parts[1]]
            case "inc":
                reg[parts[1]] += 1
            case "dec":
                reg[parts[1]] -= 1
            case "jnz":
                val = int(parts[2])
                if parts[1].isdigit():
                    if parts[1]!='0':
                        pos+=val
                        continue
                elif reg[parts[1]] != 0:
                        pos+=val
                        continue

        pos+=1

    print(reg['a'])

sim()
sim(True)