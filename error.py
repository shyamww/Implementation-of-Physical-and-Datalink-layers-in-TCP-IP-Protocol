from random import choice, randint

def error_generator(data,er):
    n = er
    m = len(data) - 1
    pos = []
    if n == 0:
        return data
    for i in range(n):
        pos.append(randint(0, m))
    ret = ""
    for i in range(m + 1):
        if i in pos:
            if data[i] == "0":
                ret += "1"
            else:
                ret += "0"
        else:
            ret += data[i]
    return ret