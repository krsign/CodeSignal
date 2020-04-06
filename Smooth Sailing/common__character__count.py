def commonCharacterCount(s1, s2):
    s3 = list(s1)
    s4 = list(s2)
    l1 = []
    for i in s3:
        if i in s4:
            l1.append(i)
            s4.remove(i)
    return len(l1)
