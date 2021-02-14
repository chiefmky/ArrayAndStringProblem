#Implement a method to perform basic string compression using count of repeated characters
#input:aabcccccaaa
#output:a2b1c5a3

def compression(astr):
    # aabcccccaa
    ch = astr[0]
    count = 1
    ans = ""

    for i in range(1, len(astr)):
        if ch == astr[i]:
            count += 1
        else:
            ans += ch + str(count)
            count = 1
        ch = astr[i]
    ans += ch + str(count)
    return ans

def compression2(astr):
    count = 0
    siz = len(astr)
    arr = []

    for i in range(siz):
        count += 1
        if i + 1 >= siz or astr[i] != astr[i + 1]:
            arr.append(astr[i])
            arr.append(count)
            count = 0
    return "".join(str(ch) for ch in arr)

if __name__ == '__main__':
    s = "aabcccccd"
    print(compression2(s))