##9.3 A magic index in an array A [0. . .n-1] is defined to be an index such that A[i]
##= i. Given a sorted array of distinct integers, write a method to find a magic
##index, if one exists, in array A.
"""
Brute force would be to iterate through array and check index against value in array
Since values are sorted and distict, this can be solved using a binary search approach
"""
def magicIndex(array, start, end):
    if start>end or start<0 or end>len(array)-1:
        return -1
    mid=(start+end)/2
    if array[mid]==mid:
        return mid
    elif array[mid]>mid:
        return magicIndex(array, start, mid)
    else:
        return magicIndex(array, mid+1, end)