
##Write a method to replace all spaces in a string with'%20'. You may assume that
##the string has sufficient space at the end of the string to hold the additional
##characters, and that you are given the "true" length of the string.
#Method1: Using built-in function
def replace1(string):
    string=string.replace(" ","%20")
    return string