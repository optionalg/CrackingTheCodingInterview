
#Method2: Convert string into list to manipulate
def replace2(string):
    string=list(string)
    for i in range(len(string)):
        if string[i]==" ":
            string[i]="%20"
    string="".join(string)
    return string