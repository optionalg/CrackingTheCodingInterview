
##Write a function to determine the number of bits required to convert integer A
##to integer B.
##EXAMPLE
##Input: 31,14
##Output: 2
def flipper(x,y):
    """
    to find the spots at which x and y differ, do an xor
    xor tells you how many bits need to be flipped and is represented by 1
    count the number of 1's now
    """
    a=x^y
    count=0
    while a!=0:
        if a&1==1:
            count+=1
        a=a>>1
    return count