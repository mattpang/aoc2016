def compress(x) -> str:
    newstring = ''
    quote_mode=False

    sample= False
    buf = ''
    seq=''
    for i,c in enumerate(x):

        if c=='(':
            if sample:
                pass
            else:
                quote_mode = True
                continue
        elif c==')':
            if quote_mode:
                quote_mode=False
                x,y = map(int,buf.split('x'))

                seq=''
                buf=''
                sample=True
                continue


        if sample:
            if x>0:
                x-=1
                seq+=c
            if x==0:
                sample=False

                newstring+=seq*y
                x = y = None
                continue
        elif quote_mode:
            buf+=c
        else:
            newstring+=c

    return newstring

assert compress('ADVENT') == 'ADVENT'
assert compress("A(1x5)BC") == "ABBBBBC"
assert compress('(3x3)XYZ') == 'XYZXYZXYZ'
assert compress('A(2x2)BCD(2x2)EFG') == 'ABCBCDEFEFG'
assert compress('(6x1)(1x3)A') == '(1x3)A'
assert compress('X(8x2)(3x3)ABCY') == 'X(3x3)ABC(3x3)ABCY'

print(len(compress(open('inputs/9.txt').read()).strip()))



def decompress(s):
    if '(' not in s:
        return len(s)
    ret = 0
    while '(' in s:
        ret += s.find('(')
        s = s[s.find('('):]
        marker = s[1:s.find(')')].split('x')
        s = s[s.find(')') + 1:]
        ret += decompress(s[:int(marker[0])]) * int(marker[1])
        s = s[int(marker[0]):]
    ret += len(s)
    return ret

assert decompress('(3x3)XYZ') == len('XYZXYZXYZ')
assert decompress('X(8x2)(3x3)ABCY') == len('XABCABCABCABCABCABCY')

print(decompress(open('inputs/9.txt').read().strip()))