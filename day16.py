def flip(x):
    # flip the bits
    t = ""
    for c in x:
        if c == "1":
            t += "0"
        elif c == "0":
            t += "1"
    return t


def expander(x: str, limit: int) -> str:
    while len(x) < limit:
        x = x + "0" + flip(x[::-1])
    return x[0:limit]


def reducer(x: str) -> str:
    
    t=[]
    for a,b in zip(x[::2],x[1::2]):
        if a==b:
            t.append('1')
        else:
            t.append('0')
    
    x=t

    if len(x)%2==0:
        x=reducer(x)

    return ''.join(x)



init = "10000"

assert expander("1", 3) == "100"

assert expander("10000", 20) == "10000011110010000111"

assert reducer('110010110100') == '100'


print(reducer(expander('11100010111110100',272)))

# part 2 is limit=35651584
print(reducer(expander('11100010111110100',35651584)))

# the pattern repeats every 36. there's room to go much faster than brute forcing it
# print(expander('11100010111110100',36))
# print(expander('11100010111110100',72))

