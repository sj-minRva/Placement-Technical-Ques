
def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse = True)
    print(A)
    print(B)
    
    for x in range(len(A)):           
        if A[x]+B[x] < k:
            return 'NO'
        else:
            return 'YES'

A = [1,0,0,1,1,1]
B = [3,1,2,1,1,1]
k = 4

result = twoArrays(k, A, B)
print(result)
