from collections import deque
from itertools import permutations

d = '''###########
#0.1.....2#
#.#######.#
#4.......3#
###########'''

d = open('inputs/24.txt').read()

grid = dict()

starting = '0' 
for y,row in enumerate(d.splitlines()):
    for x, c in enumerate(row):
        grid[(x,y)] = c


num = int(max(set(grid.values())))


stack = [] 

locations= {}

for k,v in grid.items():
    if v.isdigit():
        locations[int(v)] = k

# walk all the paths, and if we collect all numbers, we break

lengths= dict()

for place, loc in locations.items():
    paths = deque([[loc]])
    seen = set()
    seen.add(loc)
    while paths:
        curr_path = paths.popleft()
        x, y = curr_path[-1]
        if (x, y) in locations.values() and len(curr_path) > 1:
            lengths[(place, int(grid[(x,y)]))] = len(curr_path) - 1
            continue
        for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            cand = grid.get((x+dx,y+dy),'#')
            if cand!='#' and (x + dx, y + dy) not in seen:
                paths.append(curr_path + [(x + dx, y + dy)])
                seen.add((x + dx, y + dy))

print(lengths)

distances1 = []
distances2 = []


for path in permutations(range(1, num+1)):
    path = (0,) + path + (0,)
    distance = 0
    for i in range(len(path) - 2):
        distance += lengths[(path[i], path[i+1])]
    distances1.append(distance)
    distances2.append(distance + lengths[(path[-2], path[-1])])

print(min(distances1))
print(min(distances2))


