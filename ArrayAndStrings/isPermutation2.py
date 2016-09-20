#Method2: Sort both strings and compare

def isPermutation2(str1, str2):
    return sort(str1)==sort(str2)

def sort(string):
    string=list(string)
    string.sort()
    string="".join(string)
    return string