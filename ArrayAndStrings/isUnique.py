##Implement an algorithm to determine if a string has all unique characters. What
##if you cannot use additional data structures?
def isUnique(string):
    dict_={}
    for letter in string:
        if letter in dict_:
            return False
        else:
            dict_[letter]=1
    return True