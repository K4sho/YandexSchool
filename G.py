n = input()

def rle_decode(data):
    decode = ''
    count = ''
    for i in range(0, len(data)):
        if i+1 > len(data)-1 and data[i].isdigit() == False:
            decode += data[i]
            break
        if (data[i].isdigit() == False) and (data[i+1].isdigit()):
            for j in range(i+1, len(data)):
                if data[j].isdigit():
                    count += data[j]
                else:
                    break
            decode += data[i] * int(count)
            count = ''
        elif (data[i].isdigit() == False) and (data[i+1].isdigit() == False):
            decode += data[i]

    return decode
# A15BA5
# Z123XY

print(len(rle_decode(n)))
