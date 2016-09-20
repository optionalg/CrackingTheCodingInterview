
##Implement a function which reverses a nullterminated string.
def revStr(string):
    string=list(string)
    length=len(string)
    ptr1=0
    ptr2=length-1
    while ptr1<=ptr2:
        string[ptr1],string[ptr2]=string[ptr2],string[ptr1]     #swap letters
        ptr1+=1
        ptr2-=1
    string="".join(string)
    return string