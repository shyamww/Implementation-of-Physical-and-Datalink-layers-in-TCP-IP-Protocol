def encode(data):
    enc_data = ""
    #blank string
    for bit in data:
        #change 0 to 1 and -1
        if bit == "0":
            enc_data += "1-1"
        #change 1 to -1 and 1
        else:
            enc_data += "-11"
    return enc_data

def decode(data):
    bit_data = ""
    #blank string
    for i in range(0, len(data), 3):
        j = i + 3
        bit = data[i:j]
        #change 1 and -1 to 0
        if bit == "1-1":
            bit_data += "0"
        #change -1 and 1 to 1
        elif bit == "-11":
            bit_data += "1"
    return bit_data