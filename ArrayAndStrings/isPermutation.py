
##Given two strings, write a method to decide if one is a permutation of the other.
##Assumptions: (1) spaces are considered. (2) case-sensitive
#Method1: Check if both strings have the same character counts
def isPermutation1(str1, str2):
    if len(str1)!=len(str2):
        return False
    #create str1 dict
    s1={}
    for letter in str1:
        if letter in s1:
            s1[letter]+=1
        else:
            s1[letter]=1
    #compare to str2
    for letter in str2:
        if letter in s1:
            s1[letter]-=1
        else:
            return False
    #all values in s1 must be 0. False otherwise
    for val in s1.itervalues():
        if val!=0:
            return False
    return True