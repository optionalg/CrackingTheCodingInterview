
##Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
##print the binary representation. If the number cannot be represented ACCURATELY
##in binary with at most 32 characters, print "ERROR."
def binRep(num):
    """
    type num: float
    """
    if num>=1 or num<=0:
        return "ERROR"

    out=[]
    while num>0:
        if len(out)==32:
            return "ERROR"
        r=num*2
        if r>=1:
            out.append(1)
            num=r-1
        else:
            out.append(0)
            num=r
    return "".join(out)