"""
Given a string containing just the characters '(' and ')'
Return the length of the longest valid (well-formed) parentheses substring
"""

def validParen(string):   
    stack = [-1] #base index
    maxLen = 0
    for x in range(len(string)):  #current index
        if string[x] == '(':
            stack.append(x)
        else:   # string[x] == ')':
            stack.pop()
            if not stack:       #stack empty =>no match for )
                stack.append(x) #put back into the stack for future match
            else:
                length = x - stack[-1]
                maxLen = max(maxLen,length)

    return maxLen


string = input("Enter string: ")
maxLen = validParen(string)
print("Max Length of string: " + str(maxLen))

        
            
