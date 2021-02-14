# Implement an algorithm to determine if a string has all unique characters

def isUnique(myStr):
    for ch in myStr:
        if myStr.count(ch) > 1:
            return False
    return True


def isUnique2(myStr):
    hash = []
    for ch in myStr:
        if ch in hash:
            return False
        else:
            hash.append(ch)
    return True


if __name__ == '__main__':
    s = "Hello world"
    print(isUnique2(s))