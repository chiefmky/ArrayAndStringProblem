#write a method to decide if one is a permutation of the other

def isPermutation(aString, bString):
    if len(aString) != len(bString):
        return False

    for ch in aString:
        if aString.count(ch) != bString.count(ch):
            return False
    return True


def isPermutation2(aString, bString):
    if len(aString) != len(bString):
        return False
    return sorted(aString) == sorted(bString)


if __name__ == '__main__':
    a = "bale"
    b = "pale"
    print(isPermutation2(a, b))