res = []
arr = list(map(int, input("Enter the elements separated by space: ").split()))
def reverseArray(arr):
    for i in arr[ : : -1]:
        res.append(i)
    print(res)        
reverseArray(arr)
