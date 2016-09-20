##9.1 A child is running up a staircase with n steps, and can hop either 1 step, 2 steps,
##or 3 steps at a time. Implement a method to count how many possible ways the
##child can run up the stairs.
def countWaysMyMethod(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return countWaysMyMethod(n-1)+countWaysMyMethod(n-2)+countWaysMyMethod(n-3)