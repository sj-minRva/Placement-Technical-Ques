#Week 2 - assignment 2

'''
A high-security vault uses a custom PIN authentication mechanism. To reduce the chances
of brute-force attacks, the system only allows PINs that are Neon Numbers.
The rule is:
A PIN is valid if the sum of the digits of its square equals the PIN itself.
Your Task: Write a Python program that reads a numeric PIN input by the user and validates
whether it is a Neon Number or not.
'''

n = int(input("Enter pin: "))
square = n*n
print("Square: ", square)
result = 0

while square > 0:
    digit = square%10
    temp = square//10
    square = temp
    result += digit
    print(result)

if result == n:
    print("Neon Number")
else:
    print("Not Neon Number")
    
