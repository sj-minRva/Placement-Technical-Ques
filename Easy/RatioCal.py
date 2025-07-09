
n = int(input())
arr = [-4, 3, -9, 0, 4, 1]

def RatioCal(arr,n):
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            zero += 1        
    positive_ratio = positive / n
    print(f"{positive_ratio :.6f}")
    negative_ratio = negative / n
    print(f"{negative_ratio:.6f}")
    zero_ratio = zero / n
    print(f"{zero_ratio :.6f}")
        
RatioCal(arr,n)