from collections import Counter

d = """rect 6x1
rotate column x=1 by 1
rotate row y=0 by 4"""
# rotate column x=1 by 1"""
gridsize_x = 7
gridsize_y = 3

d = open('inputs/8.txt').read()
gridsize_x = 50
gridsize_y = 6

grid = Counter()

for line in d.splitlines():
    newgrid = grid.copy()

    m, out = line.split(' ',1)
    match m:
        case "rect":
            x, y = map(int,out.split("x"))

            for i in range(x):
                for j in range(y):
                    newgrid[(i, j)] = 1

        case "rotate":
            parts = out.split()
            k, v = parts[1].split("=")
            idx = int(v)
            val = int(parts[-1])
            match parts[0]:
                case "row":
                    for i in range(gridsize_x):
                        newgrid[(i, idx)] = grid[((i-val) % gridsize_x, idx)]
                case "column":
                    for i in range(gridsize_y):
                        newgrid[(idx, i)] = grid[(idx, (i - val) % gridsize_y)]
    
    grid = newgrid.copy()

print(sum(grid.values()))

t = []
for i in range(gridsize_y):
    l=''
    for j in range(gridsize_x):
        
        if grid[(j,i)] ==1 :
            l+='█'
        else:
            l+=' '
    t.append(l)

print('\n'.join(t))

