#Type Conversion
"""
birthYear = input("Enter your birth year: ")
age = 2025 - int(birthYear)
print(age)
"""


#Basic Calculator
"""
num1  = float(input("Enter the first num: "))
num2  = float(input("Enter the second num: "))
sum = num1 + num2
print("Sum: ", sum)
"""

#If statement
'''
weight = float(input("Enter weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == 'K':
    convertedWeight = weight*2.205
    print("Weight in Lbs: ", convertedWeight)
elif unit.upper()== 'L':
    convertedWeight = weight/2.205
    print("Weight in Kgs: ", convertedWeight)
else:
    print("invalid")
'''

#List

names = ["Mary", "Sid", "Sam", "Max", "Alex", "Eleven", "Mick"] #list
#slicing of strings
print(names[-2])
print(names[0:3:])
print(names[0:6:2])

print("Before change: ", names)
names[0] = "John"
print("After change: ", names)
