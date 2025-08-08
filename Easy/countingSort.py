
def countingSort(arr):
    freq = [0]*100

    for x in arr:
        freq[x] += 1

    return freq

arr = [1,1,3,2,1,0,2,10]
result = countingSort(arr)
print(result)
