#Write methods to implement the multiply, subtract, and divide operations for
#integers. Use only the add operator.
def divide(numerator, denominator):
    if denominator==0:
        return
    if denominator>numerator:
        return
    result=0
    while denominator<=numerator:
        result=result+1
        denominator=denominator+denominator
    return result
