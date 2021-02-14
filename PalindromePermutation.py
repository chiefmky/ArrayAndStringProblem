#write a function to check if it is a permutation of a palindrome

def PalindPerm(aString):
    aString = aString.replace(" ", "")
    aSet = set(aString)
    oddN = 0

    for ch in aSet:
        c = aString.count(ch)
        if c % 2 == 1:
            oddN += 1
    if oddN <= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "tact coa"
    print(PalindPerm(s))

