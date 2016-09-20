
#Method3: Manipulate string itself. Python strings are immutable though
#         Gotta rewrite string everytime space is encountered
def replace3(string):
    ptr=0
    while ptr<len(string):
        if string[ptr]==" ":
            string=string[:ptr]+"%20"+string[ptr+1:]
            ptr+=2
        ptr+=1
    return string