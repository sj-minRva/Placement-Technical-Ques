def CheckOddEven(number):
    count = 0
    nums = []
    for i in range(number):
        temp = number
        evenCount = 0
        oddCount = 0
        print(i)
        length = len(str(number))

        for j in range(length):            
            digit = i%10
            print(digit)
            if digit%2 == 0:
                evenCount+=1
            else:
                oddCount+=1
            if oddCount == evenCount:
                continue
            else:
                count+=1
                nums.append(i)
            
    print("Total count: " , count)
    print("Array: " , nums)


CheckOddEven(20)   
            
