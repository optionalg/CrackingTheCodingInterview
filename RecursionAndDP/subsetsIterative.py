##9.4 Write a method to return all subsets of a set.
import copy
#iterative
def subsetsIterative(arr):
    subset=[[]]
    for num in arr:
        dcopy=copy.deepcopy(subset)
        for i in dcopy:
            i.append(num)
        subset+=dcopy
    subset=sorted(subset,key=lambda x: len(x))
    return subset