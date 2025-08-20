# Week 4 - assignmnent 1

"""
At Insight Analytics, the DataOps team is responsible for maintaining data quality across
real-time dashboards, reports, and AI pipelines.
To streamline data handling across various components, you are tasked with implementing a
unified utility function that simplifies basic list operations. This function will be used
across multiple internal scripts to ensure consistent list behavior and efficient processing.

Problem Statement
Write a single Python function named list_util that performs different operations on a list
based on a specified command.

Function Signature
def list_util(L, command):

    ...

Parameters:
L: A list of elements.

command: A string representing the operation to perform. It can be one of:

"is_empty" – Check if the list is empty.

"first" – Get the first element of the list.

"last" – Get the last element of the list.

"init" – Get all elements except the last.

"rest" – Get all elements except the first.

Depending on the value of command, the function should perform one of the following:

If command is "is_empty", return True if the list is empty, and False otherwise.

If command is "first", return the first element of the list if it’s non-empty; otherwise return None.

If command is "last", return the last element of the list if it’s non-empty; otherwise return None.

If command is "rest", return a list of all elements except the first one, if the list is non-empty. If the list has only one element, return an empty list. If the list is empty, return None.
Example Usage:
list_util([], "is_empty")       ➞ True  
list_util([1, 2, 3], "first")   ➞ 1  
list_util([1, 2, 3], "last")    ➞ 3  
list_util([1], "init")          ➞ []  
list_util([], "rest")           ➞ None  

"""


def list_util(L, command):    
    if command == 'is_empty':
        if len(L) == 0:
            return True
        else:
            return False

    elif command == 'first':
        if L[0] == None:
            return None        
        return L[0]

    elif command == 'last':
        if L[-1] == None:
            return None
        return L[-1]
    
    elif command == 'rest':
        if not L:
            return None
        return L[1::]
    
    elif command == 'init':
        return L[:-1:]
    
    
result = list_util([1,2,3,4,5], "init")          
print(result)
        
    
            
    































    


