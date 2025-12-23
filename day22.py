d = open("inputs/22.txt").read()

disks = dict()
for line in d.splitlines()[2:]:
    name, size, used, avail, use_pct = line.split()

    size = int(size[:-1])
    avail = int(avail[:-1])
    used = int(used[:-1])
    use_pct = int(use_pct[:-1])

    name = name.replace("/dev/grid/node-", "")
    disks[name] = (size, used, avail, use_pct)


pairs = set()
for k, A in disks.items():
    for k2, B in disks.items():
        if k != k2:
            if A[1] <= B[2] and A[1] > 0:
                # print(A[0] <= B[2], A[0],B[2])
                pairs.add((k, k2))

print(len(pairs))

#  do part 2 by hand
for y in range(30):
    t='|'
    for x in range(36):
        node_name = f"x{x}-y{y}"
        
        amt = str(disks[node_name][1]).zfill(2)
        avil = str(disks[node_name][0]).zfill(2)
        t+=f'{amt}/{avil}|'

    print(t)
    print('_'*len(t))