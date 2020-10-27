def near(s1, s2):
    if len(s1) - 1 > len(s2):
        return False
    for i in range(0, len(s1)):
        test = s1[0:i:] + s1[i + 1::]
        if test == s2:
            return(True)
    else:
        return False
