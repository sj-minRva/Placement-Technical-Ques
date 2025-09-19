def removeDuplicates(nums):
   
    i = 0  
    for j in range(1, len(nums)):  
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    # i+1 is the length of unique elements
    return i + 1


nums = [1,1,2,2,3]
k = removeDuplicates(nums)
print(k)
print("Modified nums:", nums[:k])
