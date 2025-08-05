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
"""
names = ["Mary", "Sid", "Sam", "Max", "Alex", "Eleven", "Mick"] #list

#slicing of strings
print(names[-2])
print(names[0:3:])
print(names[0:6:2])

print("Before change: ", names)
names[0] = "John"
print("After change: ", names)
"""

#Opertion on List
'''
numbers = [1, 3, 4, 7, 6,34, 22, 1, 3, 9]
numbers.append("rhea")
print(numbers)

numbers.insert(0, 0)
print(numbers)

numbers.remove('rhea')
print(numbers)

numbers.pop()  # removes the last element
print(numbers)

numbers.sort()  # sorts the list
print(numbers)

numbers.reverse()  # reverses the list
print(numbers)

numbers.clear()  # clears the list
print(numbers)
'''

#Range

numbers = range(5,20,3)
print(numbers)

for i in range(5,20,2):
    print(i)

#Tuple
numbers = (1,2,3)
































