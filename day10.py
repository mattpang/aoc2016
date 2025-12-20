from collections import defaultdict

d = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''


compare = set([5,2])

d = open('inputs/10.txt').read()
compare = {61,17}


        
# print(bots)
# print(rules)

def run(part1=True):
    bots =defaultdict(list)
    outputs = dict()
    rules = dict()
    for line in d.splitlines():
        if line.startswith('value'):
            parts = line.split()
            bots[int(parts[-1])].append(int(parts[1]))

        else:
            parts = line.split()
            rules[int(parts[1])] = (parts[5], int(parts[6]) , parts[10], int(parts[11]))


    running =True
    while running:
        new_bot = bots.copy()
        for k,v in bots.items():
            if len(v) == 2:
                # apply a rule
                if set(v) == compare and part1:
                    print(k)
                    return k

                v = sorted(v)
                low_type, low_dest, high_type, high_dest = rules[k] 

                # if len(new_bot[low_dest])<2 and len(new_bot[high_dest])<2:
                if low_type=='bot':
                    if len(new_bot[low_dest])<2:
                        new_bot[low_dest].append(v[0])
                    else:
                        continue
                if high_type =='bot':
                    if len(new_bot[high_dest])<2:
                        new_bot[high_dest].append(v[1])
                    else:
                        continue

                if low_type =='output':
                    outputs[low_dest] = v[0]

                if low_type =='output':
                    outputs[low_dest] = v[0]
                    
                new_bot[k]=[]


        if outputs.get(0) and outputs.get(1) and outputs.get(2):
            print(outputs.get(0)*outputs.get(1)*outputs.get(2))
            return

        bots = new_bot.copy()

run()
run(False)