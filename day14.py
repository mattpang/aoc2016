import hashlib

def run(part2=False):
    salt = "ihaygndm"

    triples = []
    otp = []

    hashes = [] 
    for i in range(16000):
        s = salt + str(i)
        d = hashlib.md5(s.encode()).hexdigest()
        if part2:
            for j in range(2016):
                d = hashlib.md5(d.encode()).hexdigest()
        
        hashes.append(d)
        

    for i,d in enumerate(hashes):


        for a, b, c in zip(d, d[1:], d[2:]):
            if a == b == c:
                triples.append([a + b + c, i])
                break

        for t, p in triples:
            if t + t[0] + t[0] in d and (i - p) <= 1000 and (i-p)>0:
                otp.append(p)
    
        if not part2:
            if len(otp)==64:
                otp.sort()
                print(otp[-1])
                return
        
    otp.sort()
    print(otp[64])
    

run(False)
run(True)