def SelectionSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        minIdx = i
        for j in range(i+1 , n):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[minIdx] , arr[i] = arr[i] , arr[minIdx]
        
    return arr
    
arr = [2,3,1,5,4,0]
result = SelectionSort(arr)
print(result)
        
            