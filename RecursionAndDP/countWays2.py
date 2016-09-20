def countWaysBookWay(n):
    if n<0:
        return 0
    elif n==0:
        return 1
    else:
        return countWaysBookWay(n-1)+countWaysBookWay(n-2)+countWaysBookWay(n-3)