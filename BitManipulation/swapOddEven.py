
##Write a program to swap odd and even bits in an integer with as few instructions
##as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and
##soon).
def swapOddEvenBits(x):
    origNum=format(x, 'b').zfill(32)
    a=(((x&2863311530)>>1) | ((x&1431655765)<<1))
    swappedNum=format(a, 'b').zfill(32)
    print origNum
    print swappedNum
    return