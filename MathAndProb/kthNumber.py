#Design an algorithm to find the kth number such that the only prime factors are
#3,5, and 7.
#gotta memoize this
def kthNumber(k):
    kth=[]
    i=0
    while i<k:
        #for j in range(0,int(float('inf'))):
        for j in range(0,20000):
            if isfactors357(j):
                kth.append(j)
        i=i+1
    return kth[k-1]
        
'''
def isfactors357(x):
    primefactors=[]
    for i in range(1,x+1):
        if isPrime(i):
            if x%i==0:
                primefactors.append(i)
    if len(primefactors)==3:
        if 3 and 5 and 7 in primefactors:
            return True
    return False
'''

def isfactors357(x):
    '''
    factors=[]
    for i in range(1,x+1):
        if x%i==0:
            factors.append(i)
    pfactors=[]
    for i in range(0,len(factors)):
        if isPrime(factors[i]):
            pfactors.append(factors[i])
    if len(pfactors)==4:
        if 1 and 3 and 5 and 7 in pfactors:
            return True
    return False
    '''
    pfactors=primefactors(x)
    if len(pfactors)==4:
        if 1 in pfactors and 3 in pfactors and 5 in pfactors and 7 in pfactors:
            return True
    return False

def primefactors(x):
    allfactors=factors(x)
    pfactors=[]
    for i in range(0, len(allfactors)):
        if isPrime(allfactors[i]):
            pfactors.append(allfactors[i])
    return pfactors

def factors(x):
    factor=[]
    for i in range(1,x+1):
        if x%i==0:
            factor.append(i)
    return factor

def isPrime(x):
    if x==1:
        return True
    for i in range(2,x-1):
        if x%i==0:
            return False
    return True
