d = open('inputs/15.txt').read()


meta = dict()

for line in d.splitlines():
    parts = line.split()
    meta[parts[1]] = {'total_positions':int(parts[3]),'time': int(parts[6].replace(',','').split('=')[1]), 'pos': int(parts[11].replace('.',''))}

print(meta)
def run(part2=False):
    i=0
    if part2:
        meta['#7'] = {'total_positions': 11, 'time': 0, 'pos': 0}

    while True:
        for t,(k,v) in enumerate(meta.items(),1):
            if ((v['pos']+t+i) % v['total_positions']) !=0 : 
                break
        else:
            print(i)
            break
            
        i+=1
    
run()
run(part2=True)