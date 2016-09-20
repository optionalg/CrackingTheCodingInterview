#Write methods to implement the multiply, subtract, and divide operations for
#integers. Use only the add operator.
def negate(b):
    if b>0:
        base=-1
        result=0
        while b>0:
            result=result+base
            b=b-1
        return result
    elif b<0:
        base=1
        result=0
        while b<0:
            result=result+base
            b=b+1
        return result
    else:
        return 0
    
def subtract(a,b):
    result=a+negate(b)
    return result