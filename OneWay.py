#write a function to check if two strings are one edit away

def oneWay(aString, bString):
    c = 0

    for ch in aString:
        if ch not in bString:
            c += 1
    if c > 1:
        return False
    else:
        return True


# ***************************************************
# This is editing
def oneEditsWay(aString, bString):
    if len(aString) == len(bString):
        return oneEditReplace(aString, bString)
    elif len(aString) + 1 == len(bString):
        return oneEditReplace(aString, bString)
    elif len(aString) - 1 == len(bString):
        return oneEditReplace(bString, aString)
    else:
        return False


def oneEditReplace(s1, s2):
    foundDifference = False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if foundDifference:
                return False
            foundDifference = True
    return True


# *****************************************************
# inserting
def oneEditInsert(s1, s2):
    i, j = 0, 0

    while j < len(s2) and i < len(s1):
        if s1[i] != s2[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True


if __name__ == '__main__':
    s = "pale"
    t = "pae"
    print(oneEditInsert(s, t))

