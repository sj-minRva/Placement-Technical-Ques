def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums) ):
        if nums[i] != nums[j]:
            i+=2
            nums[i] = nums[j]

    print(nums)
    return i+1

nums = [1,1,1,2,2,2,3]
k = removeDuplicates(nums)
print(k)
print(nums[:k]) 
