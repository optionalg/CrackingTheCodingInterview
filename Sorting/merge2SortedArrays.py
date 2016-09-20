##11.1 You are given two sorted arrays, A and B, where A has a large enough buffer at
##the end to hold B. Write a method to merge B into A in sorted order.
a=[1,3,5,7,9,0,0,0,0,0]
b=[2,4,6,7,8]
def merge(A,B,m,n):
    ptr=len(A)-1
    ptrA=m-1
    ptrB=n-1
    while ptrA>=0 and ptrB>=0:
        if A[ptrA]>B[ptrB]:
            A[ptr]=A[ptrA]
            ptrA-=1
            ptr-=1
        else:
            A[ptr]=B[ptrB]
            ptrB-=1
            ptr-=1
    while ptrB>=0:
        A[ptr]=B[ptrB]
        ptr-=1
        ptrB-=1
    return A