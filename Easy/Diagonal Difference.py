arr = [11,2,4], [4,5,6], [10,8,-12]

def diagonalDifference(arr):
    # Write your code here
    mini = 0
    maxi = len(arr) - 1   
    rightDiagonalSum = 0
    leftDiagonalSum  = 0
    for i in range( len(arr) ):
        for j in range( len(arr[0]) ):
            if i==j:
                rightDiagonalSum += arr[i][j]

            if i == mini and j == maxi:
                leftDiagonalSum += arr[i][j]
                mini += 1
                maxi -= 1                
    AbsoluteDifference = abs(rightDiagonalSum - leftDiagonalSum)
    return AbsoluteDifference

diff = diagonalDifference(arr)
print(diff)


