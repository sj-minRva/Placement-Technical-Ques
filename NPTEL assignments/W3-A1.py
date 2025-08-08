#Week 3 - assignemnt 1

'''
n the land of Codeville, young programmers discover an ancient scroll containing
a list of mysterious words — each one part of a secret prefix code used by the town’s
old network of messengers. Legend says that hidden among these words is one with special
power: the longest word in the list. But there’s a twist — if more than one word shares
the longest length, the scroll reveals only the one that appears last in the list.The
town’s Code Scribe, Pixel, needs your help. She wants you to write a program that will
search through this list and identify the special word according to the rules.
Write a program that:

Accepts a single line of input containing a comma-separated list of words from the
ancient prefix code.

Finds and prints:
(a) The longest word in the list.
(b) If multiple words share the maximum length, print the one that appears right-most in
the list.

'''

ancientPrefix = input("Enter Ancient Prefix Code: ")
codes = ancientPrefix.split(",")
print(codes)
count = 0
for x in codes:
    count += 1
    print(count)
