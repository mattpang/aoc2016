from hashlib import md5


def starts_zeros_hash(x: str) -> bool:
    out = md5(x.encode()).hexdigest()
    return out.startswith("00000"), out


assert starts_zeros_hash("abc3231929")[0] is True


def run(p2=False):
    index = 0
    starting_code = 'uqwqemis'

    # starting_code = "abc"
    # index = 3231928

    pw = ""
    p2password = dict()
    while True:
        code = starting_code + str(index)
        res, out = starts_zeros_hash(code)
        if res:
            pw += out[5]
            if p2:
                if out[5].isdigit():
                    if 0<=int(out[5])<8 and int(out[5]) not in p2password.keys():
                        p2password[int(out[5])] = out[6]

                if len(p2password) == 8:
                    p=''
                    for i in range(8):
                        p+=p2password[i]
                    return p
                    
            else:
                if len(pw) == 8:
                    return pw
        index += 1

print(run())
print(run(p2=True))