def string_bits(str):
    newstr = ''
    for i in range(0, len(str), 2):
        newstr += str[i]
    return newstr