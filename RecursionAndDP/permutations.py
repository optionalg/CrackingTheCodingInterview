##9.5 Write a method to compute all permutations of a string.
import copy
#iterative
def permutations(string):
    string=list(string)
    perm=[string.pop()]
    for i in string:
        temp=[]
        for j in perm:
            temp.append(insertToAllPositions(j, i))
        perm=[]
        for sublist in temp:
            for item in sublist:
                perm.append(item)
    return perm

def insertToAllPositions(word, letter):
    temp=[]
    array=list(word)
    for i in range(len(array)):
        ret=copy.deepcopy(array)
        ret.insert(i, letter)
        temp.append(ret)
    ret=copy.deepcopy(array)
    ret.append(letter)
    temp.append(ret)
    for i in range(len(temp)):
        temp[i]="".join(temp[i])
    return temp