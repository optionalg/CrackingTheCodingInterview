##Given a positive integer, print the next smallest and the next largest number
##that have the same number of 1 bits in their binary representation.
def _getNext(n):
    """
    Trick is to flip a 1 to 0 and a 0 to 1. To get the next biggest number,
    what you do is
    1. Get the FIRST NON-TRAILING 0 when you read from right to left
    Mark that point as p.
    2. Get the count of 1's (c1) and 0's (c0) to the right of p
    2.5. if c1+c0==32 or ==0, return -1
    3. Flip the 0 at p (c1+c0) to 1
    4. Clear out all the bits to the right of p
    5. Add c1-1 ones at the right-most end
    """
    c=n
    c0=0
    c1=1
    while c&1==0 and c!=0:
        c0+=1
        c=c>>1
    while c&1==1 and c!=0:
        c1+=1
        c=c>>1
    #if number is 111..11000..000, no number bigger w/ same # of ones
    if c0+c1==31 or c0+c1==0:
        return -1
    p=c0+c1
    n=n^(1<<p)          #set p to 1
    n=n&~((1<<p)-1)     #set everything after p to 0
    n=n^((1<<(c1-1))-1)
    return n

def _getPrevious(n):
    """
    Just like getNext but the opposite. :D
    p is FIRST NON-TRAILING 1
    """
    c=n
    c0=0
    c1=0
    while c&1==1:
        c1+=1
        c=c>>1
    if c==0:        #check if n was 1111..1111 or 00000..0011...111
        return -1

    while c&1==0 and c!=0:
        c0+=1
        c=c>>1
    p=c0+c1
    n=n<<~(1<<(p+1)-1)      #clear from p onwards
    n=n^((1<<(c1+1)-1)<<(c0-1))
    return n

def getPrevNext(n):
    a=_getNext(n)
    b=_getPrevious(n)
    return [a,b]