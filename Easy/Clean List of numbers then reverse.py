'''after creating list of numbers, remove all duplicates and reverse the list'''

arr = [1,2,3,6,7,6,3,2,5]

def uniqueRevsersedList(arr):
    unique = []
    for i in arr:
        if i not in unique:
            unique.append(i)
    print(unique)
    rev = []
    for i in unique[ : : -1]:
        rev.append(i)

    return rev
    

rev = uniqueRevsersedList(arr)
print(rev)
