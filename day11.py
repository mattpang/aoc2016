d = '''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.'''

d=open('inputs/11.txt').read()

floors = [0,0,0,0]

for floornum, line in enumerate(d.splitlines()):
    parts = line.split()
    
    for i,p in enumerate(parts):
        if 'generator' in p or 'microchip' in p: 
            floors[floornum] += 1

print(sum(2 * sum(floors[:x]) - 3 for x in range(1,4)))
floors[0]+=4
print(sum(2 * sum(floors[:x]) - 3 for x in range(1,4)))

