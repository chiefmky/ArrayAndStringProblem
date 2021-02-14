#check if s2 is a rotation of s1 using only one call to isSubstring
def stringRotation(s1,s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        if s2 in s1s1:
            return True
        else:
            return False
    return False


if __name__ == '__main__':
    s1 = "waterbottle"
    s2 = 'boerttlewat'
    print(stringRotation(s1,s2))