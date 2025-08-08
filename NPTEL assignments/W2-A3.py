#Week 2 - assignemnt 3

'''
While analysing intercepted communications, TASC officer Srikant Tiwari suspects that some
messages might be carrying hidden signals. One of the red flags used by the agency is the
density of vowels in a message — unusually high vowel counts may indicate a coded alert.
To assist in screening these messages quickly, a script is needed to count the number of
vowels in any given string.
Write a Python program that:
Takes a message as input.
Counts the number of vowels (a, e, i, o, u — both uppercase and lowercase).
Prints the vowel count.
Input Format:
A single line containing a string .
Output Format:
A single integer — the count of vowels (A, E, I, O, U in both uppercase and lowercase).
'''

string = input("Enter msg: ")
count = 0
for x in string:
    if x in 'AEIOUaeiou':
        count += 1
print(count)
