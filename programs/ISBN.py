def ld(s):
    s = s.replace('-', '')
    s = list(map(int, s))
    l = 10 - ((
        s[0] + (3*s[1]) + s[2] + (3*s[3]) + s[4] + (3*s[5]) +
        s[6] + (3*s[7]) + s[8] + (3*s[9]) + s[10] + (3*s[11])
    ) % 10)
    return(f'{s[0]}{s[1]}{s[2]}-{s[3]}-{s[4]}{s[5]}{s[6]}-{s[7]}{s[8]}{s[9]}{s[10]}{s[11]}-{l}')
