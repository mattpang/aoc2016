from itertools import permutations

tally=0
lines = open('inputs/3.txt').read().splitlines()
for line in lines:
    w = permutations(map(int,line.split()),3)
    if all([c[0]+c[1] > c[2] for c in w]):
        tally+=1

print(tally)

pt2_tally = 0 

for i,j,k in zip(lines[::3],lines[1::3],lines[2::3]):
    
    ii = list(map(int,i.split()))
    jj = list(map(int,j.split()))
    kk = list(map(int,k.split()))

    x = [ii[0],jj[0],kk[0]]
    y = [ii[1],jj[1],kk[1]]
    z = [ii[2],jj[2],kk[2]]


    for g in [x,y,z]:
        w = permutations(g,3)
        if all([c[0]+c[1] > c[2] for c in w]):
            pt2_tally+=1

print(pt2_tally)