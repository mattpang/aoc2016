
import re 

def check(x)->bool:

    abba_cands = []

    for i in range(len(x)-3):
        if (x[i] == x[i+3]) and (x[i+1] == x[i+2]) and (x[i] != x[i+1]) and (x[i:i+2] == x[i+2:i+4][::-1]):
            abba_cands.append(x[i:i+4])

    # brackets could be multiple times. 
    bracket_groups = re.findall(r'\[(.*?)\]',x)

    for b in bracket_groups:
        for a in abba_cands:
            if a in b:
                return False
            
    if len(abba_cands)>0:
        return True
    else:
        return False

def check_ssl(x)->bool:
    # brackets could be multiple times. 
    bracket_groups = re.findall(r'\[(.*?)\]',x)

    aba_cands = []

    # remove all the bracket substrings 
    for b in bracket_groups:
        x = x.replace(b,'')
    

    substrs = x.split('[]')

    for s in substrs:
        if len(s) == 3:
            i=0
            if (s[i] == s[i+2]) and (s[i] != s[i+1]):
                aba_cands.append(s)

        for i in range(len(s)-2):
            if (s[i] == s[i+2]) and (s[i] != s[i+1]) :
                aba_cands.append(s[i:i+3])
    
    aba_cands = set(aba_cands) - set(bracket_groups)

    for b in bracket_groups:
        for a in aba_cands:
            if a[1]+a[0]+a[1] in b:
                return True
            
    return False

# check('wjzwftiuixvwyzmgoe[jbfghrqhyywwhlu]wcijbojvlgjjdtowzpv[lgfvxfdusgxddsppbxb]pagicuiuerzeydww[wlpjklgzyilrifonz]gdicckmxibtwwoesaxf')

assert check('abba[mnop]qrst') is True
assert check('abcd[bddb]xyyx') is False
assert check('aaaa[qwer]tyui') is False
assert check('ioxxoj[asdfgh]zxcvbn') is True

tally = 0 
for line in open('inputs/7.txt').read().splitlines():
    if check(line):
        tally+=1

print(tally)

assert check_ssl('aba[bab]xyz') is True
assert check_ssl('xyx[xyx]xyx') is False
assert check_ssl('aaa[kek]eke') is True
assert check_ssl('zazbz[bzb]cdb') is True

tally = 0 
for line in open('inputs/7.txt').read().splitlines():
    if check_ssl(line):
        tally+=1

print(tally)