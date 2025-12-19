
def dist(instructions:str,pt2=False):
    pos = complex(0,0)
    facing = complex(0,1)
    been = set()
    been.add(pos)
    for cmd in instructions.split(','):

        line= cmd.strip()
        if line.startswith('R'):
            facing*=-1j
        elif line.startswith('L'):
            facing*=1j
        
        steps = int(line[1:])
        for i in range(steps):
            pos += facing

            if pos in been and pt2:

                return int(abs(pos.real)+abs(pos.imag))

            been.add(pos)

    return int(abs(pos.real)+abs(pos.imag))

assert dist('R2, L3') == 5
assert dist('R2, R2, R2') == 2
assert dist('R5, L5, R5, R3') == 12

assert dist('R8, R4, R4, R8',True) == 4

d = open('inputs/1.txt').read()
print(dist(d))
print(dist(d,True))