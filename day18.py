# row = ".^^.^.^^^^"
row = open('inputs/18.txt').read().strip()

grid = dict()
y = 0
max_y = 40
max_y = 400000
last_row = dict()
safe_tiles = 0 

for x, c in enumerate(row):

    last_row[x] = c
    if c == '.':
        safe_tiles+=1

for y in range(1,max_y):
    if y==40:
        print(safe_tiles)

    this_row = dict()
    for x in range(len(row)):
        a,b,c = last_row.get(x-1,'.'), last_row.get(x,'.'), last_row.get(x+1,'.')
                
        if a=='^' and b == '.' and c=='.':
            this_row[x] = '^'
        elif a == '.' and b=='.' and c=='^':
            this_row[x] = '^'
        elif a == '^' and b=='^' and c=='.':
            this_row[x] = '^' 
        elif a == '.' and b=='^' and c=='^':
            this_row[x] = '^' 
        else:
            this_row[x] = '.'
            safe_tiles+=1
    
    last_row = this_row

print(safe_tiles)
