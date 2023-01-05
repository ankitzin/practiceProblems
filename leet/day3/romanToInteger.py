"""
value numerals are represented by seven different symbols: I, V, X, L, C, D and M.
"""


def value(r):
    if r == 'I':
        return 1
    if r == 'V':
        return 5
    if r == 'X':
        return 10
    if r == 'L':
        return 50
    if r == 'C':
        return 100
    if r == 'D':
        return 500
    if r == 'M':
        return 1000
    return -1


def rom_to_int(s:str):
    res = 0
    for i in range(0, len(s), 1):
        if i != len(s)-1 and value(s[i]) < value(s[i+1]):
            res = res + value(s[i+1]) - value(s[i])
            i = i+1
        else:
            res += value(s[i])

    return res


print(rom_to_int('III'))
