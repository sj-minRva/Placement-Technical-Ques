#Week 4 - assignment 2

"""
In the mystical realm of Numbertown, numbers are not just mathematical entities —
they possess personalities. Among them, Perfect Numbers are considered rare and noble.

A perfect number is one whose value is equal to the sum of all its proper divisors
(excluding itself).
For example:

6 = 1 + 2 + 3

Function Requirements
Write a Python function named is_perfect that:

Accepts a positive integer n as input.

Returns True if n is a perfect number.

Returns False otherwise.


Note: You do not need to read input or print output. The function will be directly called
in test cases.

You are appointed as the Royal Number Analyst and tasked with identifying whether a given
number holds this rare title.

"""

def is_perfect(n):

    divisors = []    
    for i in range(1,n):        
        if n%i == 0:            
            divisors.append(i)                
    sumOfDiv = 0
    for x in divisors:     
        sumOfDiv += x
    if sumOfDiv == n:
        return True
    else:
        return False
        
result = is_perfect(28)
print(result)

        
    
