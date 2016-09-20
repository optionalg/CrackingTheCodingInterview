
##Explain what the following code does: ((n & (n-1)) == 0).
"""
Say A=n and B=n-1
If A&B=0, that means A and B don't share a one

When you subtract 1 from n, you look for the last 1 (going left to right)
if the 1 is the absolute last digit in the number:
you do a quick subtraction,
and you're done - ex: 100011010101-1 = 100011010100
else:
keep borrowing. ex: abcde1000-1 = abcde0111

but in the above case n&n-1!=0...
for n&(n-1) to equal 0, the abcde part will also have to be 0
so n will have to be something like 0001000 in order for n&(n-1) to be 0
in other words,
the code checks if n is a power of 2
"""