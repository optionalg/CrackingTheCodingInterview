
##Implement a method to perform basic string compression using the counts
##of repeated characters. For example, the string aabcccccaaa would become
##a2blc5a3. If the "compressed" string would not become smaller than the original
##string, your method should return the original string.
#Method1: Iterate through string, copy chars to new string and count repeats
def compression(string):
    newStr=""
    ltrCnt=1
    chkLetter=string[0]
    for i in range(1,len(string)):
        if chkLetter==string[i]:
            ltrCnt+=1
        else:
            newStr+=chkLetter+str(ltrCnt)
            chkLetter=string[i]
            ltrCnt=1
    newStr+=chkLetter+str(ltrCnt)
    if len(string)>len(newStr):
        return string
    return newStr
