#Write methods to implement the multiply, subtract, and divide operations for
#integers. Use only the add operator.
def multiply(a,b):
    result =0
    count=0
    while count<b:
        result=result+a
        count=count+1
    return result