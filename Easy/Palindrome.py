# Get a string as input, check its palindrome or not, without using string handling functions.

def getLen(string):
    count = 0
    for x in string:
        count += 1
    return count

def isPalindrome(string):
    #length = getLen(string)
    i , j = 0, getLen(string)-1
    while i < j:
        if string[i] != string[j]:
            return False        
        i += 1
        j -= 1
    return True

string = input("Enter the string: ")

if isPalindrome(string) == True:
    print("Is a palindrome.")
else:
    print("Is not a  palindrome.")


    	


	
	
