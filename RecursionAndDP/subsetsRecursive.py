#recursive
subsets=[[]]
def subsetsRecursive(arr, subsets):
    if len(arr)==0:
        subsets=sorted(subsets,key=lambda x: len(x))
        return subsets
    dcopy=copy.deepcopy(subsets)
    num=arr.pop()
    for i in dcopy:
        i.append(num)
    subsets+=dcopy
    return subsetsRecursive(arr, subsets)