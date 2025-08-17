
def plusMinus(n, arr):
    countNeg = countPos = countZer = 0    
    for x in arr:
        if x < 0:
            countNeg += 1            
        if x > 0:
            countPos += 1
        if x == 0:
            countZer += 1
    NegRatio = countNeg/n
    print(f"{NegRatio :.6f}")
    PosRatio = countPos/n
    print(f"{PosRatio :.6f}")
    ZeoRatio = countZer/n
    print(f"{ZeoRatio :.6f}")


n = 6
arr = [-4, 3, -9, 0, 4, 1]
plusMinus(n, arr)
