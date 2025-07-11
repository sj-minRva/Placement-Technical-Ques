def RatioCal(arr,n):
    positive  = negative = zero = 0
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


n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements separated by space: ").split()))

if n == len(arr):
    RatioCal(arr,n)
else:
    print("Invaild array")
