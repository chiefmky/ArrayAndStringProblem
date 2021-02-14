#write a method to replace all spaces in a string with "%20"

def isURLify(aString, aSiz):
    newS = ""
    for ch in aString:
        if ch == " ":
            newS += "%20"
        else:
            newS += ch
    return newS


def isURLify2(aString, aSiz):
    return aString.replace(" ", "%20")


if __name__ == '__main__':
    s = "Mr John Smith"
    siz = 13
    print(isURLify2(s, siz))

